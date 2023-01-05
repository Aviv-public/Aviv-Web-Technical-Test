from datetime import datetime

import requests

import settings
from pricemap import logger
from pricemap.entities.listing import Listing
from pricemap.finder.geo_place_finder import GeoPlaceFinder
from pricemap.repository.listing_repository import ListingRepository


class ImportListing:
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.listing_repository = ListingRepository()

    def import_all_listings(self) -> None:
        """Import listings for all places."""
        for place_id in GeoPlaceFinder.retrieve_all_places_ids():
            logger.debug(f"Import listings for placeId {place_id}")
            self._import_listings_for(place_id)

    def _import_listings_for(self, place_id: int) -> None:
        """
        Import all listings for a given place_id.

        That method will call an external API to retrieve data
        while the API returns a 200 status code then bulk persists
        Listings entities into a dedicated table.

        Args:
            - place_id : place id used to call the external API
        """
        current_page = 1
        is_last_page = False
        while not is_last_page:
            response = requests.get(self.api_url % place_id, {"page": current_page})
            if response.status_code != 200:
                if response.status_code != 416:
                    raise Exception(
                        "Listing API returns an unexpected status code",
                        {
                            "status_code": response.status_code,
                            "response": response.text,
                        },
                    )
                break

            json_response = response.json()
            # if we've received less than paginator limit,
            # that means we reached the last page
            is_last_page = len(json_response) < settings.LISTING_API_NB_RESULTS_PER_PAGE

            logger.info(f"Import listings for placeId {place_id} - page {current_page}")

            bulk_listings = []
            for item in json_response:
                listing = Listing.from_data(item, place_id, datetime.now())
                logger.debug(f"Add listing {listing.id} to bulk")
                bulk_listings.append(listing)

            self.listing_repository.upsert_bulk(bulk_listings)
            current_page += 1

import requests
from datetime import datetime

from pricemap.entity.listing import Listing
from pricemap.finder.geo_place_finder import GeoPlaceFinder
from pricemap.repository.listing_repository import ListingRepository


class ImportListing:
    def __init__(self):
        self.listing_repository = ListingRepository()

    def import_all_listings(self):

        for geom in GeoPlaceFinder.retrieve_all_places():
            p = 0
            while True:
                p += 1
                url = "http://listingapi:5000/listings/" + str(geom) + "?page=" + str(p)
                d = requests.get(url)

                # Break when finished
                if d.status_code == 416:
                    break

                for item in d.json():
                    listing = Listing.from_data(item, geom, datetime.now())

                    self.listing_repository.insert(listing)

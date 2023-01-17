from pricemap import registry
from pricemap.controllers.listingapi import app
from factory import ListingFactory


if __name__ == "__main__":
    # FIXME: where does model init belongs ?
    registry.listing_repository_sqlite.init()
    listings = ListingFactory.build_many(10, ["fr-FR", "de-DE", "nl-BE"])
    for listing in listings:
        registry.persist_listing.perform(listing)
    app.run(debug=True, host="0.0.0.0", port=8080)

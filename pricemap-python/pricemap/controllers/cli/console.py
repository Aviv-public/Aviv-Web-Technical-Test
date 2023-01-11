#!/usr/bin/env python3

import click

from pricemap import settings
from pricemap.domain.usecases.import_all_listings import ImportAllListings
from pricemap.registry import geo_place_finder, listing_repository


@click.group()
def cli() -> None:
    pass


@cli.command()
def import_all_listings() -> None:
    """Import all listings by browsing through the listing api."""
    import_all_listings = ImportAllListings(
        settings.LISTING_API_URI, listing_repository, geo_place_finder
    )
    import_all_listings.import_all_listings()


if __name__ == "__main__":
    cli()

#!/usr/bin/env python3

import click


@click.group()
def cli() -> None:
    pass


@cli.command()
def import_all_listings() -> None:
    """Import listings by browsing through the listing api."""
    import settings
    from pricemap.usecases.import_all_listings import ImportAllListings

    import_all_listings = ImportAllListings(settings.LISTING_API_URI)
    import_all_listings.import_all_listings()


if __name__ == "__main__":
    cli()

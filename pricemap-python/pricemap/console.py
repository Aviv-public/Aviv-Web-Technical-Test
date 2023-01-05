#!/usr/bin/env python3

import click


@click.group()
def cli() -> None:
    pass


@cli.command()
def import_listings() -> None:
    """Import listings by browsing through the listing api."""
    import settings
    from pricemap.use-cases.import_listing import ImportListing

    import_listing = ImportListing(settings.LISTING_API_URI)
    import_listing.import_all_listings()


if __name__ == "__main__":
    cli()

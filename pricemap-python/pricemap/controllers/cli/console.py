#!/usr/bin/env python3

import click

from pricemap.registry import import_all_listing_usecase


@click.group()
def cli() -> None:
    pass


@cli.command()
def import_all_listings() -> None:
    """Import all listings by browsing through the listing api."""
    import_all_listing_usecase.import_all_listings()


if __name__ == "__main__":
    cli()

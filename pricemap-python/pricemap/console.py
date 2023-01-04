#!/usr/bin/env python3

import click


@click.group()
def cli():
    pass


@cli.command()
def import_listings():
    """
    Import listings by browsing through the listing api
    """
    from pricemap.usecase.import_listing import ImportListing

    ImportListing().import_all_listings()

if __name__ == '__main__':
    cli()

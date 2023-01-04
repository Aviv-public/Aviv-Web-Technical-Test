#!/usr/bin/env python3

import click
import psycopg2


@click.group()
def cli():
    pass


@cli.command()
def import_listings():
    """
    Import listings by browsing through the listing api
    """
    from pricemap.usecase.import_listing import ImportListing
    from pricemap.app import app
    from flask import g

    with app.app_context():
        if not hasattr(app, 'db'):
            app.db = psycopg2.connect(**app.config['DATABASE'])
        g.db = app.db

    ImportListing().import_all_listings()


if __name__ == '__main__':
    cli()

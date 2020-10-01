#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import Blueprint, jsonify, g

import psycopg2.extras
import json

api = Blueprint('api', __name__)


@api.route('/geoms')
def geoms():
    # FIXME: correct the sql query
    SQL = """
        SELECT
            ST_ASGEOJSON(geom) as geom,
            cog,
            -- FIXME the next line shoudl return a real price
            trunc(random() * 5000 + 5500) as price
        FROM geo_place;"""
    cursor = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(SQL)

    geoms = {
        'type': 'FeatureCollection',
        'features': []
    }
    for row in cursor:
        if not row[0]:
            continue
        geometry = {
            'type': 'Feature',
            'geometry': json.loads(row['geom']),
            'properties': {"cog": row['cog'],
                           "price": row['price']}
        }
        geoms['features'].append(geometry)
    return jsonify(geoms)


@api.route('/get_price/<path:cog>')
def get_price(cog):
    """
    Return the volumes distribution for the given cog in storage format
    """
    # FIXME
    #   - Give a better name
    #   - correct the volumes / labels fields
    serie_name = 'Dummy ' + cog
    volumes = [10, 20, 30, 40, 50]
    labels = ['0-10', '10-20', '20, 30', '30-40', '40-50']

    response = {
        'serie_name': serie_name,
        'volumes': volumes,
        'labels': labels
    }
    return jsonify(response)

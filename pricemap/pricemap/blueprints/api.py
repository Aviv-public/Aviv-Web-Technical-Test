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
    # TODO: you can tweak the query and/or the code if you think it's needed :)
    SQL = """
            SELECT
                ST_ASGEOJSON(geom) as geom,
                cog,
                sum(price) / sum(area) as price
            FROM geo_place
            JOIN listings ON geo_place.id = listings.place_id
            group by (geom, cog)
            ;"""
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
    # TODO : maybe we can do a better histogram (better, computation, better volume and labels etc...)
    serie_name = 'Prix ' + cog
    labels = {'0-6000': 0, '6000-8000': 0, '8000-10000': 0,  '10000-14000': 0, '14000-100000': 0}

    for label in labels:
        min_price = label.split('-')[0]
        max_price = label.split('-')[1]
        SQL = f"""
            SELECT
                 ST_ASGEOJSON(geom) as geom,
                 cog,
                 area,
                 price
             FROM geo_place
             JOIN listings ON geo_place.id = listings.place_id
             WHERE area != 0 AND price / area > {min_price} AND price / area < {max_price} 
             ;"""
        cursor = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(SQL)
        rows = cursor.fetchall()
        labels[label] = len(rows)

    response = {
        'serie_name': serie_name,
        'volumes': list(labels.values()),
        'labels': list(labels.keys())
    }
    return jsonify(response)

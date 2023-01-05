import json

from flask import Blueprint, Response, jsonify

from pricemap import db_pool

api = Blueprint("api", __name__)


@api.route("/geoms")
def geoms() -> "Response":
    # TODO: you can tweak the query and/or the code if you think it's needed :)
    SQL = """
            SELECT
                ST_ASGEOJSON(geom) as geom,
                cog,
                sum(price) / sum(area) as price
            FROM geo_place
            JOIN listings ON geo_place.id = listings.place_id
            GROUP BY (geom, cog)
            ;"""
    connection = db_pool.getconn()
    cursor = connection.cursor()
    cursor.execute(SQL)

    features = []
    for row in cursor:
        if not row[0]:
            continue
        geometry = {
            "type": "Feature",
            "geometry": json.loads(row["geom"]),
            "properties": {"cog": row["cog"], "price": row["price"]},
        }
        features.append(geometry)
    response = {"type": "FeatureCollection", "features": features}
    cursor.close()
    db_pool.putconn(connection)  # release the connection
    return jsonify(response)


@api.route("/get_price/<path:cog>")
def get_price(cog: int) -> "Response":
    """Return the volumes distribution for the given cog in storage format."""
    # TODO : maybe we can do a better histogram
    #  (better computation, better volume and labels, etc.)
    serie_name = f"Prix {cog}"
    labels = {
        "0-6000": 0,
        "6000-8000": 0,
        "8000-10000": 0,
        "10000-14000": 0,
        "14000-100000": 0,
    }
    connection = db_pool.getconn()
    cursor = connection.cursor()

    for label in labels:
        min_price = label.split("-")[0]
        max_price = label.split("-")[1]
        SQL = f"""
            SELECT
                 ST_ASGEOJSON(geom) as geom,
                 cog,
                 area,
                 price
             FROM geo_place
             JOIN listings ON geo_place.id = listings.place_id
             WHERE area != 0
                AND price / area > {min_price}
                AND price / area < {max_price}
             ;"""
        cursor = connection.cursor()
        cursor.execute(SQL)
        rows = cursor.fetchall()
        labels[label] = len(rows)

    response = {
        "serie_name": serie_name,
        "volumes": list(labels.values()),
        "labels": list(labels.keys()),
    }
    cursor.close()
    db_pool.putconn(connection)  # release the connection
    return jsonify(response)

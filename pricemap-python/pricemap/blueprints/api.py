import json

from flask import Blueprint, Response, jsonify

from pricemap.adapters.utils.postgres_db_pool import PostgresDbPool


api = Blueprint("api", __name__)


@api.route("/geoms")
def geoms() -> "Response":
    # TODO: you can tweak the query and/or the code if you think it's needed :)
    sql_request = """
            SELECT
                ST_ASGEOJSON(geom) as geom,
                cog,
                sum(price) / sum(area) as price
            FROM geo_place
            JOIN listing ON geo_place.id = listing.place_id
            GROUP BY (geom, cog)
            ;
    """
    features = []

    with PostgresDbPool.get_connection() as connection:
        for row in connection.execute(sql_request):
            geometry = {
                "type": "Feature",
                "geometry": json.loads(row["geom"]),
                "properties": {"cog": row["cog"], "price": row["price"]},
            }
            features.append(geometry)

    response = {"type": "FeatureCollection", "features": features}
    return jsonify(response)


@api.route("/get_price/<path:cog>")
def get_price(cog: int) -> "Response":
    """Return the volumes distribution for the given cog in storage format."""
    # TODO : maybe we can do a better histogram
    #  (better computation, better volume and labels, etc.)
    serie_name = f"Prix {cog}"
    labels: dict[str, int] = {
        "0-6000": 0,
        "6000-8000": 0,
        "8000-10000": 0,
        "10000-14000": 0,
        "14000-100000": 0,
    }

    sql_request = """
         SELECT
              count(*) as count
         FROM geo_place
         JOIN listing ON geo_place.id = listing.place_id
         WHERE area != 0
            AND cog = %(cog)s
            AND price / area >= %(min_price)s
            AND price / area <= %(max_price)s
         ;
    """

    with PostgresDbPool.get_connection() as connection:
        for label in labels:
            min_price = label.split("-")[0]
            max_price = label.split("-")[1]
            row = connection.execute(
                sql_request,
                {
                    "cog": cog,
                    "min_price": min_price,
                    "max_price": max_price,
                },
            ).fetchone()
            labels[label] = row["count"] if row else 0

    response = {
        "serie_name": serie_name,
        "volumes": list(labels.values()),
        "labels": list(labels.keys()),
    }
    return jsonify(response)

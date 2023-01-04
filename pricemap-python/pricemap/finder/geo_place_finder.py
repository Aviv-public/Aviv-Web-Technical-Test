import psycopg2
from flask import g


class GeoPlaceFinder:

    @staticmethod
    def retrieve_all_places() -> list:
        SQL = """
            SELECT DISTINCT(id)
            FROM geo_place
            ORDER BY id ASC;"""
        cursor = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(SQL)
        place_ids = []
        for row in cursor:
            if not row[0]:
                continue
            place_ids.append(row['id'])

        cursor.close()
        return place_ids

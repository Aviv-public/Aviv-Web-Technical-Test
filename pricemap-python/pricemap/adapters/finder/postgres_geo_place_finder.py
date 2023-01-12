from pricemap.adapters import db_pool
from pricemap.domain.finder.geo_place_finder import GeoPlaceFinder


class PostgresGeoPlaceFinder(GeoPlaceFinder):
    def retrieve_all_places_ids(self) -> list[int]:
        sql_request = """
            SELECT id
            FROM geo_place
            ORDER BY id ASC;
        """
        connection = db_pool.getconn()
        cursor = connection.cursor()
        try:
            cursor.execute(sql_request)
            places_ids = []
            for row in cursor:
                places_ids.append(row["id"])
        finally:
            cursor.close()
            db_pool.putconn(connection)  # release the connection
        return places_ids

from pricemap import db_pool


class GeoPlaceFinder:
    @staticmethod
    def retrieve_all_places_ids() -> list:
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

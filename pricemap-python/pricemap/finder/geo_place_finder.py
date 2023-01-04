from pricemap import db_pool

class GeoPlaceFinder:

    @staticmethod
    def retrieve_all_places() -> list:
        SQL = """
            SELECT DISTINCT(id)
            FROM geo_place
            ORDER BY id ASC;"""
        connection = db_pool.getconn()
        cursor = connection.cursor()
        cursor.execute(SQL)
        place_ids = []
        for row in cursor:
            if not row[0]:
                continue
            place_ids.append(row['id'])

        cursor.close()
        db_pool.putconn(connection) #re-put connection to db pull
        return place_ids

from pricemap.adapters.utils.postgres_db_pool import PostgresDbPool
from pricemap.domain import ports


class PostgresGeoPlaceFinder(ports.GeoPlaceFinder):
    def retrieve_all_places_ids(self) -> list[int]:
        sql_request = """
            SELECT id
            FROM geo_place
            ORDER BY id ASC;
        """

        with PostgresDbPool.get_connection() as connection:
            places_ids = []
            for row in connection.execute(sql_request):
                places_ids.append(row["id"])

        return places_ids

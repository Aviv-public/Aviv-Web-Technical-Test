import psycopg

from pricemap.adapters.utils.postgres_db_pool import PostgresDbPool
from pricemap.domain import ports
from pricemap.domain.entities.listing import Listing


class PostgresListingRepository(ports.ListingRepository):
    def upsert_bulk(self, listings: list[Listing]) -> None:
        """
        Upsert bulk of rows in listing table.

        Args:
            - listings -- List of entities to upsert
        """
        sql_request = """
            INSERT INTO public.listing(
                id,
                place_id,
                price,
                room_count,
                area,
                seen_at
            )
            VALUES (
                %(id)s,
                %(place_id)s,
                %(price)s,
                %(room_count)s,
                %(area)s,
                %(seen_at)s
            )
            ON CONFLICT (id) DO UPDATE
                SET price = EXCLUDED.price,
                    seen_at = EXCLUDED.seen_at;
        """

        with PostgresDbPool.get_connection() as connection:
            try:
                for listing in listings:
                    connection.execute(
                        sql_request,
                        {
                            "id": listing.id,
                            "place_id": listing.place_id,
                            "price": listing.price,
                            "room_count": listing.room_count,
                            "area": listing.area,
                            "seen_at": listing.seen_at,
                        },
                    )
                connection.commit()
            except (
                psycopg.errors.InFailedSqlTransaction,
                psycopg.errors.SyntaxError,
                psycopg.errors.NotNullViolation,
            ):
                connection.rollback()
                raise

import psycopg2

from pricemap.adapters import db_pool
from pricemap.domain.entities.listing import Listing
from pricemap.domain.repository.listing_repository import (
    ListingRepository as ListingRepositoryInterface,
)


class ListingRepository(ListingRepositoryInterface):
    @staticmethod
    def upsert_bulk(listings: list[Listing]) -> None:
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
        connection = db_pool.getconn()
        cursor = connection.cursor()
        try:
            for listing in listings:
                cursor.execute(
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
            psycopg2.errors.InFailedSqlTransaction,
            psycopg2.errors.SyntaxError,
            psycopg2.errors.NotNullViolation,
        ):
            connection.rollback()
            raise
        finally:
            cursor.close()
            db_pool.putconn(connection)  # release the connection

import psycopg2
from pricemap import db_pool
from pricemap.entity.listing import Listing


class ListingRepository:

    @staticmethod
    def upsert_bulk(listings: list[Listing]) -> None:
        """
        Insert new row in listing table
        If row exists, update data

        Attributes
        listing -- The entity to insert
        """
        SQL = """
            INSERT INTO public.listings(id, place_id, price, room_count, area, seen_at)
            VALUES (%(id)s, %(place_id)s, %(price)s, %(room_count)s, %(area)s, %(seen_at)s)
            ON CONFLICT (id) DO UPDATE
                SET price = %(price)s,
                    seen_at = %(seen_at)s;
            """
        connection = db_pool.getconn()
        cursor = connection.cursor()
        for listing in listings:
            cursor.execute(
                SQL, {
                    'id': listing.id,
                    'place_id': listing.place_id,
                    'price': listing.price,
                    'room_count': listing.room_count,
                    'area': listing.area,
                    'seen_at': listing.seen_at
                }
            )
        try:
            connection.commit()
        except (psycopg2.errors.InFailedSqlTransaction, psycopg2.errors.SyntaxError,
                psycopg2.errors.NotNullViolation) as caught:
            connection.rollback()
            raise Exception('Listing Repository', caught)
        finally:
            cursor.close()
            db_pool.putconn(connection)  # re-put connection to db pull

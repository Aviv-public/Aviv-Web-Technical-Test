import psycopg2.extras
from flask import g

from pricemap.entity.listing import Listing

class ListingRepository:

    @staticmethod
    def insert(listing: Listing) -> None:
        """
        Insert new row in listing table
        If row exists, update data

        Attributes
        listing -- The entity to insert
        """
        SQL = """
            INSERT INTO public.listing(id, place_id, price, room_count, area, seen_at)
            VALUES (:id, :place_id, :room_count, :area, :seen_at);
            ON CONFLICT (id) DO UPDATE"""
        cursor = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
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
            g.db.commit()

        except (psycopg2.errors.InFailedSqlTransaction, psycopg2.errors.SyntaxError,
                psycopg2.errors.NotNullViolation) as caught:
            g.db.rollback()
            raise Exception('Listing Repository', caught)
        finally:
            cursor.close()

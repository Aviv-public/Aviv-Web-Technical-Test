import psycopg

from pricemap.adapters.utils.postgres_db_pool import PostgresDbPool
from pricemap.domain import ports
from pricemap.domain.entities.listing import Listing
from pricemap.domain.exceptions.unable_to_persist_listing import UnableToPersistListing


class PostgresListingRepository(ports.ListingRepository):
    def persist(self, listing: Listing) -> None:
        """
        Persist a Listing.

        If entity exists, then Update data. Otherwise insert it

        Args:
            - listing -- Entity to persist

        Raises:
            - UnableToPersistListing : Error happens when the entity is persisted
        """
        sql_request = """
            INSERT INTO public.listing(
                 id,
                 name,
                 description,
                 building_type,
                 street_address,
                 postal_code,
                 city,
                 country_iso_2,
                 price_eur,
                 surface_area_m2,
                 room_count,
                 bedrooms_count,
                 contact_phone_number,
                 created_date,
                 updated_date
            )
            VALUES (
                %(id)s,
                %(name)s,
                %(description)s,
                %(building_type)s,
                %(street_address)s,
                %(postal_code)s,
                %(city)s,
                %(country_iso_2)s,
                %(price_eur)s,
                %(surface_area_m2)s,
                %(room_count)s,
                %(bedrooms_count)s,
                %(contact_phone_number)s,
                %(created_date)s,
                %(updated_date)s
            )
            ON CONFLICT (id) DO UPDATE
                SET price_eur = EXCLUDED.price_eur,
                    updated_date = EXCLUDED.updated_date;
        """

        with PostgresDbPool.get_connection() as connection:
            try:
                connection.execute(
                    sql_request,
                    {
                        "id": listing.id,
                        "name": listing.name,
                        "description": listing.description,
                        "building_type": listing.building_type.value,
                        "street_address": listing.street_address,
                        "postal_code": listing.postal_code,
                        "city": listing.city,
                        "country_iso_2": listing.country_iso_2,
                        "price_eur": listing.price_eur,
                        "surface_area_m2": listing.surface_area_m2,
                        "room_count": listing.room_count,
                        "bedrooms_count": listing.bedrooms_count,
                        "contact_phone_number": listing.contact_phone_number,
                        "created_date": listing.created_date.utcnow(),
                        "updated_date": listing.updated_date.utcnow(),
                    },
                )
                connection.commit()
            except (
                psycopg.errors.InFailedSqlTransaction,
                psycopg.errors.SyntaxError,
                psycopg.errors.NotNullViolation,
            ) as psycopg_exception:
                connection.rollback()
                raise UnableToPersistListing(listing, str(psycopg_exception))

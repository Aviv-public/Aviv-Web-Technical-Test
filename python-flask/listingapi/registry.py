import logging
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from listingapi import adapters, settings
from listingapi.domain import use_cases


# SqlAlchemy logging
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(_handler)


# Database connection
postgres_engine = create_engine(
    settings.DATABASE_CONNECTION_STRING,
    echo=True,
)
_session_factory = sessionmaker(autocommit=False, autoflush=True, bind=postgres_engine)
_db_session: scoped_session = scoped_session(_session_factory)


# Adapters
_sql_alchemy_listing_repository = adapters.SqlAlchemyListingRepository(_db_session)


# Use cases
persist_listing_use_case = use_cases.PersistListing(_sql_alchemy_listing_repository)
retrieve_listings_use_case = use_cases.RetrieveListings(_sql_alchemy_listing_repository)
update_listing_use_case = use_cases.UpdateListing(_sql_alchemy_listing_repository)

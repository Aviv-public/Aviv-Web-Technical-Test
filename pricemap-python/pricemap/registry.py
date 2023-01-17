import logging
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from pricemap import settings
from pricemap.adapters.repository.listings import SqlAlchemyListingRepository
from pricemap.domain.usecases.listings import (
    PersistListing,
    RetrieveListings,
    UpdateListing,
)


# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Init Repositories
postgres_engine = create_engine(
    settings.DATABASE_CONNECTION_STRING,
    echo=True,
)

_session_factory = sessionmaker(autocommit=False, autoflush=True, bind=postgres_engine)
db_session: scoped_session = scoped_session(_session_factory)

# Import Repository
sql_alchemy_listing_repository = SqlAlchemyListingRepository(db_session)

# Usecases
persist_listing = PersistListing(sql_alchemy_listing_repository)
retrieve_listings = RetrieveListings(sql_alchemy_listing_repository)
update_listing = UpdateListing(sql_alchemy_listing_repository)

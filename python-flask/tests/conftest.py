import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool

from listingapi.adapters.repository.listings import SqlAlchemyListingRepository
from listingapi.domain.ports.repository.listings import ListingRepository
from listingapi.domain.usecases.listings import PersistListing, UpdateListing


@pytest.fixture
def db_session() -> scoped_session:
    in_memory_engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    _session_factory = sessionmaker(
        autocommit=False, autoflush=True, bind=in_memory_engine
    )
    db_session: scoped_session = scoped_session(_session_factory)
    return db_session


@pytest.fixture
def listing_repository(db_session: scoped_session) -> ListingRepository:
    listing_repository = SqlAlchemyListingRepository(db_session)
    listing_repository.init()
    return listing_repository


@pytest.fixture
def persist_listing_use_case(listing_repository: ListingRepository) -> PersistListing:
    return PersistListing(listing_repository)


@pytest.fixture
def update_listing_use_case(listing_repository: ListingRepository) -> UpdateListing:
    return UpdateListing(listing_repository)

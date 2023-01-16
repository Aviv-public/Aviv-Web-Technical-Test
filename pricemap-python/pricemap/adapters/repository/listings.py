from typing import List, Dict

from sqlalchemy import (
    create_engine,
)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import StaticPool

import settings
from adapters.mappers.listings import ListingMapper
from adapters.repository.models.listings import Base, Listing as ListingModel
from domain.entities.listings import Listing as ListingEntity
from domain.exceptions.listings import ListingNotFoundException
from domain.ports.repository.listings import ListingRepository

# FIXME : using in memory sqlite db for testing
engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

_session_factory = sessionmaker(autocommit=False, autoflush=True, bind=engine)
db_session: scoped_session = scoped_session(_session_factory)


class ListingRepositorySQLite(ListingRepository):
    def init(self):
        Base.metadata.create_all(engine)

    def create(self, listing: ListingEntity) -> Dict:
        listing_entity = ListingMapper.from_entity_to_model(listing)
        db_session.add(listing_entity)
        db_session.commit()
        data = ListingMapper.from_model_to_dict(listing_entity)
        return data

    def get_all(self) -> List[Dict]:
        listing_entities = db_session.query(ListingModel).all()
        listings = [
            ListingMapper.from_model_to_dict(listing) for listing in listing_entities
        ]
        return listings

    def update(self, id_: int, listing: ListingEntity):
        existing_listing = db_session.query(ListingModel).get(id_)
        if existing_listing is None:
            raise ListingNotFoundException

        listing_model = ListingMapper.from_entity_to_model(listing)
        listing_model.id = id_
        db_session.merge(listing_model)
        db_session.commit()

        listing_dict = ListingMapper.from_model_to_dict(listing_model)
        return listing_dict

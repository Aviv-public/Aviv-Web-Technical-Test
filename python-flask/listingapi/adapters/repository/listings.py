from typing import Dict, List

from sqlalchemy.orm import scoped_session

from listingapi.adapters.mappers.listings import ListingMapper
from listingapi.adapters.repository.models.listings import Base, ListingModel
from listingapi.domain.entities.listings import ListingEntity
from listingapi.domain.exceptions.listings import ListingNotFoundException
from listingapi.domain.ports.repository.listings import ListingRepository


class SqlAlchemyListingRepository(ListingRepository):
    def __init__(self, db_session: scoped_session):
        self.db_session = db_session

    def init(self) -> None:
        Base.metadata.create_all(self.db_session.get_bind())

    def create(self, listing: ListingEntity) -> Dict:
        listing_entity = ListingMapper.from_entity_to_model(listing)
        self.db_session.add(listing_entity)
        self.db_session.commit()
        data = ListingMapper.from_model_to_dict(listing_entity)
        return data

    def get_all(self) -> List[Dict]:
        listing_entities = self.db_session.query(ListingModel).all()
        listings = [
            ListingMapper.from_model_to_dict(listing) for listing in listing_entities
        ]
        return listings

    def update(self, id_: int, listing: ListingEntity) -> Dict:
        existing_listing = self.db_session.query(ListingModel).get(id_)
        if existing_listing is None:
            raise ListingNotFoundException

        listing_model = ListingMapper.from_entity_to_model(listing)
        listing_model.id = id_
        self.db_session.merge(listing_model)
        self.db_session.commit()

        listing_dict = ListingMapper.from_model_to_dict(listing_model)
        return listing_dict

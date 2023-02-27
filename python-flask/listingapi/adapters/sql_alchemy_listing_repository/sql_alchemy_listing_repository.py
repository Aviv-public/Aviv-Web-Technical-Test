from sqlalchemy.orm import scoped_session

from listingapi.adapters.sql_alchemy_listing_repository import mappers, models
from listingapi.domain import entities, ports
from listingapi.domain.entities import exceptions


class SqlAlchemyListingRepository(ports.ListingRepository):
    def __init__(self, db_session: scoped_session):
        self.db_session = db_session

    def init(self) -> None:
        models.Base.metadata.create_all(self.db_session.get_bind())

    def create(self, listing: entities.ListingEntity) -> dict:
        listing_model = mappers.ListingMapper.from_entity_to_model(listing)
        self.db_session.add(listing_model)
        self.db_session.commit()
        data = mappers.ListingMapper.from_model_to_dict(listing_model)
        return data

    def get_all(self) -> list[dict]:
        listing_models = self.db_session.query(models.ListingModel).all()
        listings = [
            mappers.ListingMapper.from_model_to_dict(listing)
            for listing in listing_models
        ]
        return listings

    def update(self, listing_id: int, listing: entities.ListingEntity) -> dict:
        existing_listing = self.db_session.get(models.ListingModel, listing_id)
        if existing_listing is None:
            raise exceptions.ListingNotFound
        self.db_session.delete(existing_listing)

        listing_model = mappers.ListingMapper.from_entity_to_model(listing)
        listing_model.id = listing_id
        self.db_session.add(listing_model)
        self.db_session.commit()

        listing_dict = mappers.ListingMapper.from_model_to_dict(listing_model)
        return listing_dict

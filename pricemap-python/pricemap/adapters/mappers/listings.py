from pricemap.adapters.repository.models.listings import ListingModel
from pricemap.domain.entities.listings import ListingEntity


class ListingMapper:
    @staticmethod
    def from_dict_to_entity(data: dict) -> ListingEntity:
        listing = ListingEntity(
            name=data["name"],
            street_address=data["postal_address"]["street_address"],
            postal_code=data["postal_address"]["postal_code"],
            city=data["postal_address"]["city"],
            country=data["postal_address"]["country"],
            description=data["description"],
            building_type=data["building_type"],
            price=data["price"]["price_eur"],
            price_date=data["price"]["date_posted"],
            surface_area_m2=data["surface_area_m2"],
            rooms_count=data["rooms_count"],
            bedrooms_count=data["bedrooms_count"],
        )
        return listing

    @staticmethod
    def from_entity_to_model(listing: ListingEntity) -> ListingModel:
        listing_model = ListingModel(
            name=listing.name,
            street_address=listing.postal_address.street_address,
            postal_code=listing.postal_address.postal_code,
            city=listing.postal_address.city,
            country=listing.postal_address.country,
            description=listing.description,
            building_type=listing.building_type,
            price=listing.price.price_eur,
            surface_area_m2=listing.surface_area_m2,
            rooms_count=listing.rooms_count,
            bedrooms_count=listing.bedrooms_count,
            contact_phone_number=listing.contact_phone_number,
        )
        return listing_model

    @staticmethod
    def from_model_to_dict(listing: ListingModel) -> dict:
        listing_dict = {
            "id": listing.id,
            "name": listing.name,
            "postal_address": {
                "street_address": listing.street_address,
                "postal_code": listing.postal_code,
                "city": listing.city,
                "country": listing.country,
            },
            "description": listing.description,
            "building_type": listing.building_type,
            "price": {
                "price_eur": listing.price,
                "created_date": listing.price_date,
            },
            "surface_area_m2": listing.surface_area_m2,
            "rooms_count": listing.rooms_count,
            "bedrooms_count": listing.bedrooms_count,
            "contact_phone_number": listing.contact_phone_number,
            "created_date": listing.created_date,
            "updated_date": listing.updated_date,
        }
        return listing_dict

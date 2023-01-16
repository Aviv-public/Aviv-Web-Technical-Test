from datetime import datetime

from pricemap.domain.entities.listing import BuildingType, Listing


class ListingMapper:
    @classmethod
    def from_dict_to_entity(cls, data: dict) -> "Listing":
        """
        Instantiate Listing Entity from Dictionary data.

        Args:
            - data -- dict that contains all input

        Returns:
            - Listing - Built Listing entities after data extraction
        """
        listing = Listing(
            data["id"],
            data["name"],
            data["description"],
            BuildingType(data["building_type"]),
            data["street_address"],
            data["postal_code"],
            data["city"],
            data["country_iso_2"],
            int(data["price_eur"]),
            int(data["surface_area_m2"]),
            int(data["room_count"]),
            int(data["bedrooms_count"]),
            data["contact_phone_number"],
            datetime.now(),
            datetime.now(),
        )

        return listing

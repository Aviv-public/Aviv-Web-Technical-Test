from pydantic import BaseModel


class PostalAddressEntity(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str

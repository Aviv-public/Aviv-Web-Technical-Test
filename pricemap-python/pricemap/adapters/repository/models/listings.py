from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class ListingModel(Base):
    __tablename__ = "listing"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    created_date: datetime = Column(
        DateTime, default=lambda: datetime.utcnow(), nullable=False
    )
    updated_date: datetime = Column(
        DateTime,
        default=lambda: datetime.utcnow(),
        onupdate=lambda: datetime.utcnow(),
        nullable=False,
    )

    # characteristics
    name: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    building_type: str = Column(String, nullable=False)
    surface_area_m2: float = Column(Float, nullable=False)
    rooms_count: int = Column(Integer, nullable=False)
    bedrooms_count: int = Column(Integer, nullable=False)

    # price
    price: float = Column(Float, nullable=False)

    # postal address
    street_address: str = Column(String, nullable=False)
    postal_code: str = Column(String, nullable=False)
    city: str = Column(String, nullable=False)
    country: str = Column(String, nullable=False)

    # contact
    contact_phone_number: Optional[str] = Column(String, nullable=True, default=None)

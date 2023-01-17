from datetime import date, datetime
from typing import TypeAlias

from sqlalchemy import Column, Date, DateTime, Float, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class ListingModel(Base):
    __tablename__ = "listing"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # characteristics
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    building_type = Column(String, nullable=False)
    surface_area_m2 = Column(Float, nullable=False)
    rooms_count = Column(Integer, nullable=False)
    bedrooms_count = Column(Integer, nullable=False)

    # price
    price = Column(Float, nullable=False)
    price_date = Column(Date, default=date.today, onupdate=date.today)

    # postal address
    street_address = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

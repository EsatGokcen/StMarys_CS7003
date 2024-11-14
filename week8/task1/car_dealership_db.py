from sqlalchemy import create_engine, Table, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Create an engine that stores data in the local directory's ecommerce.db file
engine = create_engine('sqlite:///car_dealership.db')

# Base class for classes definitions
Base = declarative_base()

# Define the customer class
class Cars(Base):
    __tablename__ = 'cars'

    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    mileage = Column(Integer, nullable=False)
    date_added = Column(DateTime, nullable=False)

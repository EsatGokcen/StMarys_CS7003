from sqlalchemy import create_engine, Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Create an engine that stores data in the local directory's ecommerce.db file
engine = create_engine('sqlite:///car_dealership.db')

# Base class for classes definitions
Base = declarative_base()
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, and_
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Create an engine that stores data in the local directory's car_dealership.db file
engine = create_engine('sqlite:///car_dealership.db')

# Base class for classes definitions
Base = declarative_base()

# Define the cars class
class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    mileage = Column(Float, nullable=False)
    date_added = Column(String, nullable=False)

# Define the salespersons class
class SalesPersons(Base):
    __tablename__ = 'salespersons'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)

# Define the sales class
class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, nullable=False, primary_key=True)
    car = Column(String, nullable=False)
    salesperson = Column(String, nullable=False)
    sale_date = Column(String, nullable=False)
    sale_price = Column(Integer, nullable=False)

# Create all tables in the engine​
Base.metadata.create_all(engine)

# Create a new session​
Session = sessionmaker(bind=engine)
session = Session()

# Add Cars to Cars table
car1 = Cars(make = 'Toyota', model = 'Camry', year = 2018, price = 18000, mileage = 31000.00, date_added = '15/01/2023')
car2 = Cars(make = 'Honda', model = 'Civic', year = 2019, price = 19500, mileage = 22000.00, date_added = '20/02/2023')
car3 = Cars(make = 'Ford', model = 'Focus', year = 2017, price = 15000, mileage = 45000.00, date_added = '10/03/2023')
car4 = Cars(make = 'Renault', model = 'Clio', year = 2021, price = 25000, mileage = 10000.00, date_added = '10/06/2024')
car5 = Cars(make = 'Skoda', model = 'Octavia', year = 2020, price = 21500, mileage = 18000.00, date_added = '23/09/2024')

session.add_all([car1, car2, car3, car4, car5])
session.commit()

# Add Salespersons to Salespersons table
salesperson1 = SalesPersons(name = 'Callum Jones')
salesperson2 = SalesPersons(name = 'Malcom Brenner')
salesperson3 = SalesPersons(name = 'Jennifer Finnegan')
salesperson4 = SalesPersons(name = 'Martin Yates')

session.add_all([salesperson1, salesperson2, salesperson3, salesperson4])
session.commit()

# Remove the Database after Queries complete.

os.remove('car_dealership.db')
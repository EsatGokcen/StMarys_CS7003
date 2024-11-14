from sqlalchemy import create_engine, Table, Column, Integer, String, Float, and_
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os

# Create an engine that stores data in the local directory's car_dealership.db file
engine = create_engine('sqlite:///car_dealership.db')

# Base class for classes definitions
Base = declarative_base()

# Association table for relationships between classes 

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

    # Relationships 

    sales = relationship('Sales', back_populates='Cars') # one-to-many relationship

# Define the salespersons class
class SalesPersons(Base):
    __tablename__ = 'salespersons'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)

    # Relationships

    sales = relationship('Sales', back_populates='Salespersons') # one-to-many relationship

# Define the sales class
class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, nullable=False, primary_key=True)
    car = Column(String, nullable=False)
    salesperson = Column(String, nullable=False)
    sale_date = Column(String, nullable=False)
    sale_price = Column(Integer, nullable=False)

    # Relationships

    car = relationship('Cars', back_populates='Sales') # many-to-one relationship with the Car class​
    salesperson = relationship('Salespersons', back_populates='Sales') # many-to-one relationship with the Salesperson class. 

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

# Add Sales info to Sales table
sale1 = Sales(car = 'Toyota', salesperson = 'Callum Jones', sale_date = '05/04/2023', sale_price = 17500)
sale2 = Sales(car = 'Honda', salesperson = 'Malcom Brenner', sale_date = '10/05/2023', sale_price = 19000)
sale3 = Sales(car = 'Ford', salesperson = 'Jennifer Finnegan', sale_date = '30/03/2024', sale_price = 36500)
sale4 = Sales(car = 'Renault', salesperson = 'Martin Yates', sale_date = '28/05/2024', sale_price = 6520)
sale5 = Sales(car = 'Skoda', salesperson = 'Malcom Brenner', sale_date = '05/07/2024', sale_price = 41000)
sale6 = Sales(car = 'Toyota', salesperson = 'Jennifer Finnegan', sale_date = '30/08/2024', sale_price = 23800)
sale7 = Sales(car = 'Ford', salesperson = 'Callum Jones', sale_date = '02/09/2024', sale_price = 31300)
sale8 = Sales(car = 'Ford', salesperson = 'Martin Yates', sale_date = '19/09/2024', sale_price = 41200)

session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8])
session.commit()

# Print tables​

cars = session.query(Cars).all()
print("\nCars:")
for car in cars:
    print(f"ID: {car.id}, Make: {car.make}, Model: {car.model}, Year: {car.year}, Price: {car.price}, Mileage: {car.mileage}, Date Added: {car.date_added}")

salespersons = session.query(SalesPersons).all()
print("\nSalespersons:")
for salesperson in salespersons:
    print(f"ID: {salesperson.id}, Name: {salesperson.name}")

sales = session.query(Sales).all()
print("\nSales:")
for sale in sales:
    print(f"Car ID: {sale.car_id}, Salesperson ID: {sale.salesperson_id}, Sale date: {sale.sale_date}, Sale price: {sale.sale_price}")

#Query the Data

# Remove the Database after Queries complete.

os.remove('car_dealership.db')
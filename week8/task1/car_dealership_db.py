from sqlalchemy import create_engine, Table, Column, Integer, String, Float, DateTime, and_
from sqlalchemy.orm import declarative_base, sessionmaker

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
    price = Column(Integer, nullable=False)
    mileage = Column(Float, nullable=False)
    date_added = Column(DateTime, nullable=False)

# Create all tables in the engine​
Base.metadata.create_all(engine)

# Create a new session​
Session = sessionmaker(bind=engine)
session = Session()

# Add Cars
car1 = Cars(make = 'Toyota', model = 'Camry', year = 2018, price = 18000, mileage = 31000.00, date_added = '15/01/2023')
car2 = Cars(make = 'Honda', model = 'Civic', year = 2019, price = 19500, mileage = 22000.00, date_added = '20/02/2023')
car3 = Cars(make = 'Ford', model = 'Focus', year = 2017, price = 15000, mileage = 45000.00, date_added = '10/03/2023')
car4 = Cars(make = 'Renault', model = 'Clio', year = 2021, price = 25000, mileage = 10000.00, date_added = '10/06/2024')
car5 = Cars(make = 'Skoda', model = 'Octavia', year = 2020, price = 21500, mileage = 18000.00, date_added = '23/09/2024')

session.add_all([car1, car2, car3, car4, car5])
session.commit()

# Query the data:
# Toyota cars manufactured after 2015 with price less than £20000

specific_cars1 = session.query(Cars).filter(and_(Cars.year > 2015, Cars.price < 20000)).first()
print(f'\n{specific_cars1.make}, {specific_cars1.model}, {specific_cars1.year}, {specific_cars1.price}, {specific_cars1.mileage}, {specific_cars1.date_added}.')
# Toyota or Honda cars with price less than £20000 and mileage below 50000
# Cars added to the database between 1st January 2023 and 31st December 2023
# Cars with mileage between 10000 and 50000 ​​
# Cars where the model's name contains 'Cl’
# Cars where the price is not null
# Cars that either Toyota, Honda, or Ford
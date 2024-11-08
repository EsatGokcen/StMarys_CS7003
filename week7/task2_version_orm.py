# TASK 2 ecommerce.db add data and query

from sqlalchemy import create_engine, Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Create an engine that stores data in the local directory's ecommerce.db file
engine = create_engine('sqlite:///ecommerce.db')

# Base class for classes definitions
Base = declarative_base()

# Association table for the many-to-many relationship between orders and products​
order_product_table = Table('order_products', Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id')),
    Column('product_id', Integer, ForeignKey('products.id')))

# Define the customer class
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

# Relationship to the order class
orders = relationship('Order', back_populates='customer')

# Define the Product class​
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    # Relationship to the Order class through the order_product_table​
    orders = relationship('Order', secondary=order_product_table, back_populates='products')

# Define the Order class​
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Relationship to the Customer class​
    customer = relationship('Customer', back_populates='orders')

    # Relationship to the Product class through the order_product_table​
    products = relationship('Product', secondary=order_product_table, back_populates='orders')

# Create all tables in the engine​
Base.metadata.create_all(engine)

# Create a new session​
Session = sessionmaker(bind=engine)
session = Session()

# Add customers​
customer1 = Customer(name='James Bond', email='bond@awl.com')
customer2 = Customer(name='Alicia Arnold', email='ali@yahoo.com')
customer3 = Customer(name = 'Jonny Stecchino', email = 'j.stec@virgilio.com')
customer4 = Customer(name = 'Brenda Willow', email = 'will@blue.com')

session.add_all([customer1, customer2, customer3, customer4])
session.commit()

# Add products​
product1 = Product(name='Laptop', price=852.5)
product2 = Product(name='Smartphone', price=312.9)
product3 = Product(name = 'Headset', price = 25.3)
product4 = Product(name = 'Tablet', price = 150.0)

session.add_all([product1, product2, product3, product4])
session.commit()

# Create orders​
order1 = Order(customer=customer1)
order1.products.append(product1)
order1.products.append(product2)
session.add(order1)

order2 = Order(customer=customer2)
order2.products.append(product3)
order2.products.append(product2)
session.add(order2)

order3 = Order(customer=customer3)
order3.products.append(product4)
session.add(order3)

order4 = Order(customer=customer4)
order4.products.append(product1)
order4.products.append(product2)
order4.products.append(product4)
session.add(order4)

session.commit()
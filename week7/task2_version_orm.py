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


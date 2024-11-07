# PP slide 45
# TASK 2 ecommerce.db add data and query

# CONNECTING TO DATABASE

from sqlalchemy import create_engine, inspect, select, MetaData, Table, Column, Integer, String, Float

engine = create_engine('sqlite://ecommerce.db', echo=False)
metadata = MetaData()

# CREATING THE TABLES

customers = Table('customers', metadata,
                  Column('customer_name',String, primary_key=True),
                  Column('customer_email', String)
)

products = Table('products', metadata,
                 Column('product', String, primary_key=True),
                 Column('price', Float)
)

orders = Table('orders', metadata,
               Column('order_id', Integer, primary_key=True),
               Column('customer_name', String),
               Column('orders', String)
)

metadata.create_all(engine)

#CHECKING TABLE IS CREATED IN DATABASE

inspector = inspect(engine)
tables = inspector.get_table_names()

# INSERTING DATA INTO THE SYSTEM

with engine.connect() as connection:
    trans = connection.begin()
    try:
        connection.execute(customers.insert(), [
            {'customer_name': 'James Bond', 'customer_email': 'bond@awl.com'},
            {'customer_name': 'Alicia Arnold', 'customer_email': 'ali@yahoo.com'},
            {'customer_name': 'Jonny Stecchino', 'customer_email': 'j.stec@virgilio.com'},
            {'customer_name': 'Brenda Willow', 'customer_email': 'will@blue.com​'}
        ])
        trans.commit()
        print("\nData inserted successfully in table employees'")
    except:
        trans.rollback()
        print("Transaction rolled back")
    
    try:
        connection.execute(products.insert(), [
            {'product': 'Laptop', 'price': 852.5},
            {'product': 'Smartphone', 'price': 312.9},
            {'product': 'Headset', 'price': 25.3},
            {'product': 'Tablet', 'price': 150}
        ])
        trans.commit()
        print("\nData inserted successfully in table employees'")
    except:
        trans.rollback()
        print("Transaction rolled back")
    
    try:
        connection.execute(orders.insert(), [
            {'order_id': 1, 'customer_name': 'James Bond', 'orders': 'Laptop, Smartphone'},
            {'order_id': 2, 'customer_name': 'Alicia Arnold', 'orders': 'Headset, Smartphone'},
            {'order_id': 3, 'customer_name': 'Jonny Stecchino', 'orders': 'Tablet'},
            {'order_id': 4, 'customer_name': 'Brenda Willow', 'orders': 'Laptop, Smartphone, Tablet'}
        ])
        trans.commit()
        print("\nData inserted successfully in table employees'")
    except:
        trans.rollback()
        print("Transaction rolled back")
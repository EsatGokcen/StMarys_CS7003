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
        connection.execute(students.insert(), [
            {'student_name': 'Alice Cooper', 'modules': 'Mathematics, Data Science'},
            {'student_name': 'Robert Ludlum', 'modules': 'Mathematics, Robotics'},
            {'student_name': 'Anita Kapur', 'modules': 'Artificial Inteligence, Robotics'},
            {'student_name': 'James Colburn', 'modules': 'Data Science, Artificial Inteligence'}
        ])
        trans.commit()
        print("\nData inserted successfully in table employees'")
    except:
        trans.commit()
        print("Transaction rolled back")
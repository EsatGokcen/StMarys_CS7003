#SQLAlchemy slide 19 
# - you will practice how to create a table insert data, and query the data.

# CONNECTING TO DATABASE

from sqlalchemy import create_engine, inspect, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite://example.db', echo=False)
metadata = MetaData()

# CREATING A TABLE

employees = Table('employees', metadata,
                  Column('id',Integer, primary_key=True),
                  Column('first_name', String),
                  Column('last_name', String))

metadata.create_all(engine)

#CHECKING TABLE IS CREATED IN DATABASE

inspector = inspect(engine)
tables = inspector.get_table_names()

# INSERTING DATA INTO THE SYSTEM

with engine.connect() as connection:
    trans = connection.begin()
    try:
        connection.execute(employees.insert(), [
            {'first_name': 'Alex', 'last_name': 'Graham'},
            {'first_name': 'Bobby', 'last_name': 'Bowl'}
        ])
        trans.commit()
        print("\nData inserted successfully in table employees'")
    except:
        trans.commit()
        print("Transaction rolled back")





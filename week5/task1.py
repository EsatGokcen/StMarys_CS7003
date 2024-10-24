#SQLAlchemy slide 19 
# - you will practice how to create a table insert data, and query the data.

from sqlalchemy import create_engine, inspect, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite://example.db', echo=False)
metadata = MetaData()

employees = Table('employees', metadata,
                  Column('id',Integer, primary_key=True),
                  Column('first_name', String),
                  Column('last_name', String))

metadata.create_all(engine)

inspector = inspect(engine)
tables = inspector.get_table_names()
print(tables)





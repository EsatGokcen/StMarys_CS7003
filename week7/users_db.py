# TASK = write a python code that: 
#   - connects to a SQlite database "user.db"
#   - insert the following data in the table "users" (week7 PP slide 36)
#   - queries the table and prints the results

# CONNECTING TO DATABASE

from sqlalchemy import create_engine, inspect, select, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite://user.db', echo=False)
metadata = MetaData()

# CREATING A TABLE

users = Table('users', metadata,
                  Column('user_name',String, primary_key=True),
                  Column('user_age', Integer),
                  Column('user_job', String))

metadata.create_all(engine)

#CHECKING TABLE IS CREATED IN DATABASE

inspector = inspect(engine)
tables = inspector.get_table_names()

# INSERTING DATA INTO THE SYSTEM

with engine.connect() as connection:
    trans = connection.begin()
    try:
        connection.execute(users.insert(), [
            {'user_name': 'Alexandra Hamilton', 'user_age': 50, 'user_job': 'Data analyst'},
            {'user_name': 'Mark Hanson', 'user_age': 65, 'user_job': 'Cybersecurity consultant'},
            {'user_name': 'Monica Geller', 'user_age': 31, 'user_job': 'Software engineer'},
            {'user_name': 'Sheldon Cooper', 'user_age': 27, 'user_job': 'Computing modeler'}
        ])
        trans.commit()
        print("\nData inserted successfully in table employees'")
    except:
        trans.commit()
        print("Transaction rolled back")
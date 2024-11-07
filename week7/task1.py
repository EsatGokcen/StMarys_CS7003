# PP slide 45
# Enrol students on different modules and remove students from modules

# CONNECTING TO DATABASE

from sqlalchemy import create_engine, inspect, select, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite://example.db', echo=False)
metadata = MetaData()

# CREATING A TABLE

students = Table('students', metadata,
                  Column('student_name',String, primary_key=True),
                  Column('modules', String),
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

# QUERY DATA

with engine.connect() as connection:
    stmt = select(students)
    result = connection.execute(stmt)
    rows = result.fetchall()
    print("\nTable employees':")
    for row in rows:
        print(row)

# you can write the same code using sqlalchemy orm which is more sophisticated and better
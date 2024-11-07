# PP slide 45
# task 1 Enrol students on different modules and remove students from modules

# CONNECTING TO DATABASE

from sqlalchemy import create_engine, inspect, select, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite://students.db', echo=False)
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
        trans.rollback()
        print("Transaction rolled back")

# QUERY DATA

with engine.connect() as connection:
    stmt = select(students)
    result = connection.execute(stmt)
    rows = result.fetchall()
    print("\nTable students':")
    for row in rows:
        print(row)

# NOT SURE HOW TO CHECK IF STUDENT ... IS ENROLLED IN MODULE ... , REMOVE STUDENT, 
student = None # NOT FINISHED
if student in students: # NOT FINISHED
    print("Removed student ... from module ...") # NOT FINISHED
else: # NOT FINISHED
    print("The student ... is not enrolled in module ...") # NOT FINISHED

# you can write the same code using sqlalchemy orm which is more sophisticated and better
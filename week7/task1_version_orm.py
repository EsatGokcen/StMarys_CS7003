from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'sqlite:///enrolment.db'

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class Enrolment(Base):
    __tablename__ = "enrolments"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    module = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

with session.begin():
    new_enrolments = [
        Enrolment(name='Alice Cooper', module="Mathmatics, Data Science"),
        Enrolment(name='Robert Ludlum', module="Mathematics, Robotics"),
        Enrolment(name='Anita Kapur', module="Artificial Intelligence, Robotics" ),
        Enrolment(name='James Colburn', module="Data Science, Artificial Intelligence")
    ]
    for enrolee in new_enrolments:
       session.add(enrolee)

    session.commit()

# Commit the transaction
session.commit()

for user in session.query(Enrolment).all():
    print(f"Name: {user.name}, Module: {user.module}")

# NOT SURE HOW TO CHECK IF STUDENT ... IS ENROLLED IN MODULE ... , REMOVE STUDENT, 
student = None # NOT FINISHED
students = 'table' #NOT FINISHED
if student in students: # NOT FINISHED
    print("Removed student ... from module ...") # NOT FINISHED
else: # NOT FINISHED
    print("The student ... is not enrolled in module ...") # NOT FINISHED

# --@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--
#                              SOLUTION
# --@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--@--

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Create an engine that stores data in the local directory's university.db file​
engine = create_engine('sqlite:///university.db')

# Base class for our classes definitions.​
Base = declarative_base()

# Association table for the many-to-many relationship between students and courses.​
enrolment_table = Table('enrolments', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('module_id', Integer, ForeignKey('modules.id'))
)

# Define the Student class​
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relationship to the Course class through the enrollment table.​
    modules = relationship('Module', secondary=enrolment_table, back_populates='students')

# Define the Module class​

class Module(Base):
    __tablename__ = 'modules'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    # Relationship to the Student class through the enrollment table.​
    students = relationship('Student', secondary=enrolment_table, back_populates='modules')

# Create all tables in the engine​
Base.metadata.create_all(engine)

# Create a new session​
Session = sessionmaker(bind=engine)
session = Session()

# Add students​
student1 = Student(name = 'Alice Cooper')
student2 = Student(name = 'Robert Ludlum')
student3 = Student(name = 'Anita Kapur')
student4 = Student(name = 'James Colburn')

session.add_all([student1, student2, student3, student4])
session.commit()

# Add modules​
module1 = Module(title = 'Mathematics')
module2 = Module(title = 'Robotics')
module3 = Module(title = 'Artifical Intelligence')
module4 = Module(title = 'Data Science')

session.add_all([module1, module2, module3, module4])
session.commit()

# Enrol students in modules​
student1.modules.append(module1)
student1.modules.append(module4)
student2.modules.append(module1)
student2.modules.append(module2)
student3.modules.append(module3)
student3.modules.append(module2)
student4.modules.append(module4)
student4.modules.append(module3)

session.commit()

# Query the database.​
for student in session.query(Student).all():
    print(f'{student.name} is enrolled in:')
    for module in student.modules:
        print(f'  - {module.title}')

# Retrieve the student and module objects​
student = session.query(Student).filter_by(name='Robert Ludlum').first()
module = session.query(Module).filter_by(title='Mathematics').first()

# Remove the module from the student's modules list.​
if module in student.modules:
    student.modules.remove(module)
    session.commit()
    print(f'\nRemoved {module.title} from {student.name}\'s modules.')
else:
    print(f'{student.name} is not enrolled in {module.title}.')


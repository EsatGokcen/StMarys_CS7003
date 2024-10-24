#SQLAlchemy slide 19 
# - you will practice how to create two tables, insert data, and query data from both tables simultaneously

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, inspect, select, insert

# CREATE AN ENGINE AND METADATA OBJECT

engine = create_engine('sqlite://library.db', echo=False)
metadata = MetaData()

# DEFINE THE "AUTHORS" TABLE

authors = Table('authors', metadata,
                Column('id', ))

# DEFINE THE "BOOKS" TABLE

#CREATE THE TABLES IN THE DATABASE

metadata.create_all(engine)

# USE THE INSPECTOR ......

# INSERT DATA INTO THE AUTHORS TABLE
#with engine...

# COMMIT THE TRANSACTION

# ROLLBACK THE TRANSACTION IN CASE OF ERROR......

# QUERY THE DATABASE

# SHOW CONTENT OF  'AUTHORS' TABLE

with engine.connect() as conn:
    result = conn.execute(select(authors))
    print("\nAuthors Table:")
    for row in result:
        print(row)

#SHOW CONTENT OF 'BOOKS' TABLE

with engine.connect() as conn:
    result = conn.execute(select(books))
    print("\nBooks Table:")
    for row in result:
        print(row)

#SHOW A BOOK AND ITS AUTHOR
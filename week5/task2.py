#SQLAlchemy slide 19 
# - you will practice how to create two tables, insert data, and query data from both tables simultaneously

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, inspect, select, insert

# CREATE AN ENGINE AND METADATA OBJECT

engine = create_engine('sqlite://library.db', echo=False)
metadata = MetaData()

# DEFINE THE "AUTHORS" TABLE

authors = Table('authors', metadata,
                Column('id', Integer, primary_key=True),
                Column('name' , String, nullable=False)
                )

# DEFINE THE "BOOKS" TABLE

books = Table('books', metadata,
              Column('id', Integer, primary_key=True),
              Column('title', String, nullable=False),
              Column('author_id', Integer, ForeignKey('authors.id'))
              )

#CREATE THE TABLES IN THE DATABASE

metadata.create_all(engine)

# USE THE INSPECTOR TO GET TABLE NAMES

inspector = inspect(engine)
tables = inspector.get_table_names()

# CHECK IF 'AUTHORS' AND 'BOOKS' TABLES EXIST

if 'authors' in tables:
    print("Table 'authors' exists in the database.")
else:
    print("Table 'authors' does not exist in the database.")

if 'books' in tables:
    print("Table 'books' exists in the database.")
else:
    print("Table 'books' does not exist in the database.")

# INSERT DATA INTO THE AUTHORS TABLE

with engine.connect() as conn: #open a connection
    trans = conn.begin() #begin a transaction
    try:
        conn.execute(insert(authors), [
            {'name': 'J.K. Rowling'},
            {'name': 'J.R.R Tolkien'}
        ])
        trans.commit() #commit the transaction
        print("\nData inserted succesfully in the table 'authors'")
    except:
        trans.rollback() # Rollback the transaction in case of error
        print("Transaction rolled back")

# INSERT DATA INTO THE BOOKS TABLE 

with engine.connect() as conn: #open a connection
    trans = conn.begin() #begin a transaction
    try:
        conn.execute(insert(books), [
            {'title': 'Harry Potter and the Philosopher\'s Stone', 'author_id': 1},
            {'title': 'The Hobbit', 'author_id': 2}
        ])
        trans.commit() #commit the transaction
        print("\nData inserted succesfully in the table 'books'")
    except:
        trans.rollback() # Rollback the transaction in case of error
        print("Transaction rolled back")

# QUERY THE DATABASE
# SHOW CONTENT OF 'AUTHORS' TABLE

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

with engine.connect() as conn:
    result = conn.execute(select(books.c.title, authors.c.name).select_from(
        books.join(authors, books.c.author_id == authors.c.id)
    ))
    for row in result:
        print(f"\nBook: {row[0]}, Authors: {row[1]}")
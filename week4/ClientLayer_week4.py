
#connect to the SQLite database and query the database about all the tasks stored in the database

import sqlite3

def create_connection(db_file): #create a database connection to the SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except sqlite3.Error as e:
        print(e)
        return conn 

def select_all_tasks(conn): #Query all rows in the tasks table
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = "user-tasks.db"

    #create a database connection

    conn = create_connection(database)
    with conn:
        print("Tasks abd tgeur priorities are:")
        print("{:<5} {:<30} {:<10}".format("nb","task","priority"))
        select_all_tasks(conn)

    def select_all_tasks(conn):
        cur = conn.cursor()
        cur.execute("SELECT id, name, priority FROM tasks")

        rows = cur.fetchall()

        for row in rows:
            print("{:<5} {:<30} {:<10}".format(row[0],row[1],row[2]))

    if __name__ == '__main__':
        main()
      
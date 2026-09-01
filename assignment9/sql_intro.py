import os
import sqlite3

os.makedirs("db", exist_ok=True)


# TASK 3 - POPULATE TABLES WITH DATA (Reusing existing connection cursor)

def add_subscriber(cursor, name, age, address):
    try:
        cursor.execute("""
            INSERT INTO subscribers (name, age, address)
            VALUES (?, ?, ?)
        """, (name, age, address))
        print(f"Subscriber '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Failed to add subscriber: {e}")

def add_publisher(cursor, name):
    try:
        cursor.execute("""
            INSERT INTO publishers (name)
            VALUES (?)
        """, (name,))
        print(f"Publisher '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Failed to add publisher: {e}")

def add_magazine(cursor, name):
    try:
        cursor.execute("""
            INSERT INTO magazines (name)
            VALUES (?)
        """, (name,))
        print(f"Magazine '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Failed to add magazine: {e}")


# MAIN EXECUTION

try:
    with sqlite3.connect("db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # TASK 2 - Create Tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publishers_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            publishers_id INTEGER,
            name TEXT NOT NULL UNIQUE,
            FOREIGN KEY (publishers_id) REFERENCES publishers (publishers_id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscribers_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            age INTEGER,
            address TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscriptions_id INTEGER PRIMARY KEY,
            publishers_id INTEGER,
            magazines_id INTEGER,
            subscribers_id INTEGER,
            FOREIGN KEY (publishers_id) REFERENCES publishers (publishers_id),
            FOREIGN KEY (magazines_id) REFERENCES magazines (magazine_id),
            FOREIGN KEY (subscribers_id) REFERENCES subscribers (subscribers_id)
        );
        """)

        print("Tables created successfully.")

        # INSERTING DATA INTO TABLES
        add_publisher(cursor, 'Conde Nast')
        add_publisher(cursor, 'Time USA')
        add_publisher(cursor, 'Hearst Communications')

        add_magazine(cursor, 'Elle')
        add_magazine(cursor, 'Vogue')
        add_magazine(cursor, 'Cosmopolitan')

        add_subscriber(cursor, 'Daphne', 20, 'New Jersey')
        add_subscriber(cursor, 'Eloise', 25, 'New York')
        add_subscriber(cursor, 'Francesca', 30, 'Philadelphia')

        conn.commit()

        # TASK 4 - EXECUTING SQL QUERIES

        cursor.execute("SELECT * FROM subscribers;")
        for row in cursor.fetchall():
            print(row)

        cursor.execute("SELECT name FROM magazines ORDER BY name;")
        for row in cursor.fetchall():
            print(row[0])

        query = """
        SELECT 
            magazines.name AS magazine_name, 
            publishers.name AS publisher_name
        FROM magazines
        JOIN publishers 
            ON magazines.publishers_id = publishers.publishers_id
        WHERE publishers.name = 'Conde Nast';
        """
        cursor.execute(query)
        for row in cursor.fetchall():
            print(f"Magazine: {row[0]} | Publisher: {row[1]}")

except sqlite3.Error as e:
    print(f"An error occurred while connecting to the database: {e}")
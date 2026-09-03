import os
import sqlite3

os.makedirs("db", exist_ok=True)

try:
    with sqlite3.connect("db/orders.db") as conn:
        print("Database has been created!")

except sqlite3.Error as e:
    print(f"An error occurred while connecting to the database: {e}")
"""
testing sqlite3 python
"""

import sqlite3

connection = sqlite3.connect('reuters.db')
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS
    stores(store_id INTEGER PRIMARY KEY, location TEXT)
    """
)

cursor.execute(
    """
    INSERT INTO stores VALUES 
    (21, 'Minneapolis, MN')
    """
)

cursor.execute("SELECT * FROM stores")

results = cursor.fetchall()
print(results)
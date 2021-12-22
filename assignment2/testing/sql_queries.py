"""
Shoaib Laghari
Coursera Data Science at Scale Specialization
Assignment 2
11/25/21
"""

import sqlite3

connection = sqlite3.connect('reuters.db')
cursor = connection.cursor()

cursor.execute(
    """
    SELECT * FROM Frequency
    """
)

results = cursor.fetchall()
print(results)
'''
John Detloff
Module 12
Big Data
Exercise 17.2
'''


import sqlite3
connection = sqlite3.connect('books.db')
import pandas as pd

cursor = connection.cursor()
cursor = cursor.execute("SELECT * FROM titles")
print(pd.read_sql('SELECT * FROM titles ORDER BY title ASC', connection))
print()


print("Description function:")
print(cursor.description)

print()
print("Fecthall() function:")
for i in cursor.fetchall():
    print(i)


    


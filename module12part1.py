'''
John Detloff
Module 12
Big Data
'''

import sqlite3
connection = sqlite3.connect('books.db')

import pandas as pd

print("Part A) Authors ordered by Last Name (descending):")
print(pd.read_sql('SELECT * FROM authors ORDER BY last DESC', connection, index_col = ['id']))
print()

print("Part B) Books ordered by Title (ascending)")
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))
print()

print("Part C) Inner Join")
print(pd.read_sql('SELECT * FROM authors INNER JOIN titles ORDER BY title ASC', connection).head())
print()

print("Part D) Insert Function")
cursor = connection.cursor()
cursor = cursor.execute("INSERT INTO authors (first, last) VALUES ('John', 'Detloff')")
print(pd.read_sql('SELECT * FROM authors ORDER BY last DESC', connection, index_col = ['id']))
print()

print("Part E) Insert Function")
cursor = cursor.execute("INSERT INTO author_ISBN(id, isbn) VALUES ('1', '1382647893')")
cursor = cursor.execute("INSERT INTO titles(isbn, title, edition, copyright) VALUES ('1382647893', 'Example Title', '1', '2022')")
print(pd.read_sql('SELECT * FROM author_ISBN ORDER BY id DESC', connection).head())
print()
print(pd.read_sql('SELECT * FROM titles ORDER BY copyright DESC', connection).head())
print()


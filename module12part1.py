'''
John Detloff
Module 12
Big Data
Exercise 17.1
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

'''
output:
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/detlo/Documents/College of DuPage Classes/CIS 2532 Python Projects/module12part1.py 
Part A) Authors ordered by Last Name (descending):
        first    last
id                   
5   Alexander    Wald
4         Dan   Quirk
1        Paul  Deitel
2      Harvey  Deitel
3       Abbey  Deitel

Part B) Books ordered by Title (ascending)
                              title
0         Android 6 for Programmers
1            Android How to Program
2                  C How to Program
3                C++ How to Program
4     Internet & WWW How to Program
5     Intro to Python for CS and DS
6               Java How to Program
7  Visual Basic 2012 How to Program
8          Visual C# How to Program
9         Visual C++ How to Program

Part C) Inner Join
   id      first    last  ...                      title edition  copyright
0   1       Paul  Deitel  ...  Android 6 for Programmers       3       2016
1   2     Harvey  Deitel  ...  Android 6 for Programmers       3       2016
2   3      Abbey  Deitel  ...  Android 6 for Programmers       3       2016
3   4        Dan   Quirk  ...  Android 6 for Programmers       3       2016
4   5  Alexander    Wald  ...  Android 6 for Programmers       3       2016

[5 rows x 7 columns]

Part D) Insert Function
        first     last
id                    
5   Alexander     Wald
4         Dan    Quirk
6        John  Detloff
1        Paul   Deitel
2      Harvey   Deitel
3       Abbey   Deitel

Part E) Insert Function
   id        isbn
0   5  0134289366
1   4  0136151574
2   3  0133406954
3   3  0132151006
4   2  0136151574

         isbn                          title  edition copyright
0  1382647893                  Example Title        1      2022
1  0135404673  Intro to Python for CS and DS        1      2020
2  0134743350            Java How to Program       11      2018
3  0134601548       Visual C# How to Program        6      2017
4  0134448235             C++ How to Program       10      2017

>>> 
'''


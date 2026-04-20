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


    
'''
output:
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/detlo/Documents/College of DuPage Classes/CIS 2532 Python Projects/module12part2.py 
         isbn                             title  edition copyright
0  0134289366         Android 6 for Programmers        3      2016
1  0134444302            Android How to Program        3      2017
2  0133976890                  C How to Program        8      2016
3  0134448235                C++ How to Program       10      2017
4  0132151006     Internet & WWW How to Program        5      2012
5  0135404673     Intro to Python for CS and DS        1      2020
6  0134743350               Java How to Program       11      2018
7  0133406954  Visual Basic 2012 How to Program        6      2014
8  0134601548          Visual C# How to Program        6      2017
9  0136151574         Visual C++ How to Program        2      2008

Description function:
(('isbn', None, None, None, None, None, None), ('title', None, None, None, None, None, None), ('edition', None, None, None, None, None, None), ('copyright', None, None, None, None, None, None))

Fecthall() function:
('0135404673', 'Intro to Python for CS and DS', 1, '2020')
('0132151006', 'Internet & WWW How to Program', 5, '2012')
('0134743350', 'Java How to Program', 11, '2018')
('0133976890', 'C How to Program', 8, '2016')
('0133406954', 'Visual Basic 2012 How to Program', 6, '2014')
('0134601548', 'Visual C# How to Program', 6, '2017')
('0136151574', 'Visual C++ How to Program', 2, '2008')
('0134448235', 'C++ How to Program', 10, '2017')
('0134444302', 'Android How to Program', 3, '2017')
('0134289366', 'Android 6 for Programmers', 3, '2016')
>>>
'''

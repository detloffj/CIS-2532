'''
John Detloff
Module 2
Introduction to using numpy
'''


import numpy as np

a = np.arange(1, 16, 1)
print(a)
print()
a= a.reshape(3, 5)
print(a)
print()

print("Row 2:, ", a[2])
print()
print("Column 4:, ", a[:, 4])
print()
print("Rows 1 & 2: ", a[1:])
print()
print("Columns 2-4: ", a[:, 2:4])
print()
print("Element(1, 4): ", a[1, 4])
print()
print("Elements from rows 1 & 2 that are in Columns 0, 2, & 4:", a[1:, [0, 2, 4]])

'''
John Detloff
Module 2 Part 2
Continuing to explore numpy
'''

import numpy as np
import csv
from scipy import stats
import statistics as st
import matplotlib.pyplot as plt

with open('C:\\Users\\detlo\\Documents\\College of DuPage Classes\\CIS 2532 Python Projects\\Student_Grades.csv', 'r') as f:
    grades = list(csv.reader(f, delimiter = ","))

grades = np.array(grades[1:], dtype =np.float64)
print(grades)
print("Number of Students: ", grades.shape[0])
print("Number of Rows & Columns: ", grades.shape)
print("Date Type: ", grades.dtype)
print("Min Percentage Score: ", grades[:, 31].min())
print("Max Percentage Score: ", grades[:, 31].max())
print("Mean of Percentage Scores: ", grades[:, 31].mean())
print("Median of Percentage Scores: ", st.median(grades[:, 31]))
m = stats.mode(grades[:, 31])
print("Mode of Percentage Scores: ", m[0])
print("Standard Deviation of Percentage Scores: ", grades[:, 31].std())
print("25th Percentile of Percentage Scores: ", np.percentile(grades[:, 31], 25))
print("75th Percentile of Percentage Scores: ", np.percentile(grades[:, 31], 75))

print()
print("Number of students in each grade catagory:")
A = grades[:, 31] > 90
print("A: ", grades[A, :].shape[0])

B = (grades[:, 31] > 80)
print("B: ", grades[B, :].shape[0] - grades[A, :].shape[0])

C = (grades[:, 31] > 70)
print("C: ", grades[C, :].shape[0] - grades[B, :].shape[0])


D = (grades[:, 31] > 60)
print("D: ", grades[D, :].shape[0] - grades[C, :].shape[0])

F = grades[:, 31] < 60
print("F: ", grades[F, :].shape[0])

results = [grades[A, :].shape[0], grades[B, :].shape[0] - grades[A, :].shape[0], grades[C, :].shape[0] - grades[B, :].shape[0], grades[D, :].shape[0] - grades[C, :].shape[0], grades[F, :].shape[0]]
results_labels = ['A stds','B stds', 'C stds', 'D stds', 'F stds']
plt.pie(results, labels = results_labels)
plt.title("Grades")
plt.show()






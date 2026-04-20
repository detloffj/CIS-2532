'''
John Detloff
Module 4
Data Visualization
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csv
from numpy import mean

data = pd.read_csv('workerstips.csv')
tips = pd.DataFrame(data)

partA = sns.scatterplot(x='total_bill', y='tip', data = tips)
partA.set(xlabel = 'Total Bill ($)', ylabel = 'Tip Amount ($)')
plt.title("Part A: Bill Amount vs. Tip Amount")
plt.show()


partB = sns.scatterplot(x='total_bill', y='tip', data = tips, hue='smoker', size = 'size')
partB.set(xlabel = 'Total Bill ($)', ylabel = 'Tip Amount ($)')
plt.title("Part B: Bill Amount vs. Tip Amount Classified by Smoker/Non-Smoker")
plt.show()


partC = sns.barplot(x = 'day', y = 'tip', data = tips, estimator = mean, order = ['Thur', 'Fri', "Sat", "Sun"])
plt.title("Part C: Average Tip Based on Day of Week")
partC.set(xlabel = 'Day', ylabel = 'Average Tip Amount ($)')
plt.show()

partD = sns.boxplot(x = 'day', y ='tip', hue ='time', data = tips,  order = ['Thur', 'Fri', "Sat", "Sun"])
plt.title("Part D: Boxplot on Tip Amount based on Day and Time")
partD.set(xlabel = 'Day', ylabel = 'Tip Amount ($)')
plt.show()

data = pd.read_csv('flightsData.csv')
flights = pd.DataFrame(data)
partE = sns.lineplot(data = flights, x = 'year', y = 'passengers', estimator = mean)
plt.title("Average Number of Passengers per Month")
plt.show()

data = pd.read_csv('titanic.csv')
titanic = pd.DataFrame(data)
partF = sns.catplot(x= 'passengerClass', data =titanic, hue = 'sex', col ='survived', kind = 'count')
plt.show()

'''
John Detloff
Module 3
Data Series and Data Frame using Pandas
'''
import numpy as np
import pandas as pd

print("Part A: \n")
lst = pd.Series([7,11,13,17])
print(lst)
print()
lst = pd.Series(100.0, index=[0, 1, 2, 3 , 4])
print(lst)
print()
lst = pd.Series(np.random.randint(0,100,20))
print(lst)
print()
print(lst.describe())
print()
temps = pd.Series([98.6, 98.9, 100.2, 97.9], index = ['Julie', 'Charlie', 'Sam', 'Andrea'])
print(temps, '\n')
dictionary = {'Julie':98.6, 'Charlie':98.9, 'Sam':100.2, 'Andrea':97.9}
temps = pd.Series(dictionary)
print(temps, '\n')
print("Part B: \n")
dictionary = {'Maxine':[98.2, 97.9, 98.1], 'James':[98.5,97.6,98.6], 'Amanda':[98.9, 99.1, 99.0]}
temps = pd.DataFrame(dictionary)
print(temps, '\n')
newTemps = pd.DataFrame(dictionary, index = ['Morning', 'Afternooon', 'Evening'])
print(newTemps, '\n')
print(newTemps['Maxine'], '\n')
print(newTemps.loc['Morning'], '\n')
print(newTemps.loc[['Morning', 'Evening']], '\n')
print(newTemps[['Maxine', 'Amanda']], '\n')
print(newTemps[['Maxine', 'Amanda']].loc[['Morning', 'Evening']], '\n')
print(newTemps.describe(), '\n')
print(newTemps.T, '\n')
print(newTemps.sort_index(axis = 1),  '\n')



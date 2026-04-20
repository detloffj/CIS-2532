'''
John Detloff
Analysis using Pandas
Module 3
'''

import csv
import pandas as pd

data = pd.read_csv('titanic.csv')
df = pd.DataFrame(data)
print(df.head())
print()
rows = df.shape[0]
print("Number of Passengers:", (rows + 1))
print()
print("Number of Passengers by Sex:")
malePass = df.loc[df['sex'] == 'male'].shape[0]
print('Male:', malePass)
femPass = df.loc[df['sex'] == 'female'].shape[0]
print('Female:', femPass)

print()
age_col = df.loc[1:, ['age']]
print("Average Age of Passengers:")
print(age_col.describe().stack()[['mean']])
print()

youth = df.loc[df["age"] < 21].shape[0]
print("Number of Passengers Younger than 21: ", youth)
tot_surv = df.loc[df['survived'] == 'yes'].shape[0]
print("Total Survivors: ", tot_surv)
males = df.loc[df['sex'] == 'male']
maleSurv = males.loc[males['survived'] == 'yes'].shape[0]
print("Total Male Survivors: ", maleSurv)
females = df.loc[df['sex'] == 'female']
femaleSurv = females.loc[females['survived'] == 'yes'].shape[0]
print("Total Female Survivors: ", femaleSurv)
tot_dec = df.loc[df['survived'] == 'no'].shape[0]
print("Total Deceased: ", tot_dec)
male_dec = males.loc[males['survived'] == 'no'].shape[0]
print("Total Males Deceased: ", male_dec)
fem_dec = females.loc[females['survived'] == 'no'].shape[0]
print("Total Females Deceased: " , fem_dec)
print()

print("Ages of Youngest and Oldest Survivors:")
surv = df.loc[df['survived'] == 'yes']


minV = (surv['age'].min())
print("Age of Youngest Survivor: ", str(format(minV, '.2f')), " years old")
minIndex = (df.index[df['age'] == minV])
x = (df.loc[minIndex,"Name"].values[0])
print("Name of Youngest Survivor: ", x)
print()

maxV = (surv['age'].max())
print("Age of Oldest Survivor: ", str(format(maxV, '.2f')), " years old")
maxIndex = (df.index[df['age'] == maxV])
x = (df.loc[maxIndex,"Name"].values[0])
print("Name of Oldest Survivor: ", x)
print()

print("List of Survivors:")



lst = surv['Name'].tolist()
y = 0
for x in lst:
    print(x)
    y+=1
    if y == tot_surv:
        break







import pandas as pd 


data = pd.read_csv('2010-2019 Fall Marathons.csv')
# print(data.loc[data["Name"].duplicated()])


# print(data.loc[data["Name"] == 'Erin Penley'])
print(data.loc[data["Age"] == 116])


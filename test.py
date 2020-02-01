import pandas as pd

data = pd.read_csv("./Processed_Data/SchoolStats/school_2015.csv")

data['School'] = data['School'].replace('( NCAA)', '', regex=True)

data['School'] = data['School'].replace('(State)', 'St', regex=True)

print(data)

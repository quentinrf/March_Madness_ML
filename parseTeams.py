import pandas as pd

data_kaggle = pd.read_csv("./Data/KaggleData/Teams.csv")
data_other = pd.read_csv("./Data/RegSeasonStats/MMStats_1993.csv")

kaggleTeams = []
otherTeams = []

for id, name in data_other["School"].iteritems():
    otherTeams.append(name)

for id, name in data_kaggle["TeamName"].iteritems():
    kaggleTeams.append(name)

print("Missing values in first list:", (set(otherTeams).difference(kaggleTeams))) 

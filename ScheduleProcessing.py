import pandas as pd

schedule = pd.read_csv("Data/RegularSeasonResults.csv")

schedule = schedule.loc[schedule['Season'] >= 2010]

schedule = schedule.loc[:, ['Season', 'WTeamID', 'LTeamID']]

schedule['Winner'] = schedule['WTeamID'] > schedule['LTeamID']

for i in range(0,schedule.shape[0]):
    if (schedule.iloc[i,3] == True):
        schedule.iloc[i, 3] = 1
    else:
        schedule.iloc[i, 3] = 0


for i in range(0,schedule.shape[0]):
    if (schedule.iloc[i,1] > schedule.iloc[i, 2]):
        temp = schedule.iloc[i,1]
        schedule.iloc[i,1] =  schedule.iloc[i,2]
        schedule.iloc[i,2] =  temp

schedule.columns = ['Season', 'Team0', 'Team1', 'Winner']

schedule.to_csv('allRegSeasonGames.csv')


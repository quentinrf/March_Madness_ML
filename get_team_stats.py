import pandas as pd
import numpy as np

def getTeamStats(Team1, Team2):
    team1_stats = list()
    team2_stats = list()
    data = pd.read_csv("Relevant_Data/mergedStats_2019.csv")
    #for row,
    team1_stats = list(data.loc[data["School"]==Team1,np.isin(data.columns, ["School", "Season"], invert=True)].values)
    team2_stats = list(data.loc[data["School"]==Team2,np.isin(data.columns, ["School", "Season"], invert=True)].values)

    #file = open("teamStats.txt", "w+")
    # for element in team1_stats:
    #     file.write(str(element) + "\n")



    print(np.asarray(list(team1_stats[0]) + list(team2_stats[0])))
    #print(team1_stats)
    #print(team2_stats)

getTeamStats("Liberty", "Louisiana Tech")

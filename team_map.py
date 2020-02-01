import pandas as pd

#---------CREATE MAP--------
data = pd.read_csv("Data/KaggleData/Teams.csv")
map = dict(zip(data.TeamID, data.TeamName))


reg_season_games = pd.read_csv("Processed_Data/allRegSeasonGames.csv")

#-----------------TEAM0-----------------
team0_names = list()
for value in reg_season_games['Team0']:
    team0_names.append(map.get(value))
reg_season_games["Team0"] = team0_names


#-----------------TEAM1-----------------
team1_names = list()
for value in reg_season_games['Team1']:
    team1_names.append(map.get(value))
reg_season_games["Team1"] = team1_names

reg_season_games.to_csv("Processed_Data/regSeasonGames.csv", index = False)

##########  IMPORTS  ##############

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

import math
import CSV
import random

#############  Load CSVs  ###############

# import xTrain and yTrain data sets

############ Train Model  ###############

############ Test Model  #################

############ Test Games for bracket  ###########

def predictGame(team1VectorIn, team2VectorIn, modelIn):


def findWinner(team1, team2, modelIn):
    year = 2019
    teamVectors = loadTeamVectors(year)[0]
    team1Vector = teamVectors[int(teams_pd[teams_pd["TeamName"] == team1].values[0][0])]
    team2Vector = teamVectors[int(teams_pd[teams_pd["TeamName"] == team2].values[0][0])]
    prediction = predictGame
    if(prediction < 0.5):
        return(team2)
    else:
        return(team1)


######## BRACKET #########
# East
game1EWinner = findWinner("Duke", "North Dakota", trainedModel)
game2EWinner = findWinner("VA Commonwealth", "UCF", trainedModel)
game3EWinner = findWinner("Mississippi St", "Liberty", trainedModel)
game4EWinner = findWinner("Virginia Tech", "St Louis", trainedModel)
game5EWinner = findWinner("Maryland", "Belmont", trainedModel)
game6EWinner = findWinner("LSU", "Yale", trainedModel)
game7EWinner = findWinner("Louisville", "Minnesota", trainedModel)
game8EWinner = findWinner("Michigan St", "Bradley", trainedModel)

game9EWinner = findWinner(game1EWinner, game2EWinner, trainedModel)
game10EWinner = findWinner(game3EWinner, game4EWinner, trainedModel)
game11EWinner = findWinner(game5EWinner, game6EWinner, trainedModel)
game12EWinner = findWinner(game7EWinner, game8EWinner, trainedModel)

game13EWinner = findWinner(game9EWinner, game10EWinner, trainedModel)
game14EWinner = findWinner(game11EWinner, game12EWinner, trainedModel)

game15EWinner = findWinner(game13EWinner, game14EWinner, trainedModel)

# West
game1WWinner = findWinner("Gonzaga", "F Dickinson", trainedModel)
game2WWinner = findWinner("Syracuse", "Baylor", trainedModel)
game3WWinner = findWinner("Marquette", "Murray St", trainedModel)
game4WWinner = findWinner("Florida St", "Vermont", trainedModel)
game5WWinner = findWinner("Buffalo", "Arizona St", trainedModel)
game6WWinner = findWinner("Texas Tech", "N Kentucky", trainedModel)
game7WWinner = findWinner("Nevada", "Florida", trainedModel)
game8WWinner = findWinner("Michigan", "Montana", trainedModel)

game9WWinner = findWinner(game1WWinner, game2WWinner, trainedModel)
game10WWinner = findWinner(game3WWinner, game4WWinner, trainedModel)
game11WWinner = findWinner(game5WWinner, game6WWinner, trainedModel)
game12WWinner = findWinner(game7WWinner, game8WWinner, trainedModel)

game13WWinner = findWinner(game9WWinner, game10WWinner, trainedModel)
game14WWinner = findWinner(game11WWinner, game12WWinner, trainedModel)

game15WWinner = findWinner(game13WWinner, game14WWinner, trainedModel)

# South
game1SWinner = findWinner("Virginia", "Gardner Webb", trainedModel)
game2SWinner = findWinner("Mississippi", "Oklahoma", trainedModel)
game3SWinner = findWinner("Wisconsin", "Oregon", trainedModel)
game4SWinner = findWinner("Kansas St", "UC Irvine", trainedModel)
game5SWinner = findWinner("Villanova", "St Mary's CA", trainedModel)
game6SWinner = findWinner("Purdue", "Old Dominion", trainedModel)
game7SWinner = findWinner("Cincinati", "Iowa", trainedModel)
game8SWinner = findWinner("Tennessee", "Colgate", trainedModel)

game9SWinner = findWinner(game1SWinner, game2SWinner, trainedModel)
game10SWinner = findWinner(game3SWinner, game4SWinner, trainedModel)
game11SWinner = findWinner(game5SWinner, game6SWinner, trainedModel)
game12SWinner = findWinner(game7SWinner, game8SWinner, trainedModel)

game13SWinner = findWinner(game9SWinner, game10SWinner, trainedModel)
game14SWinner = findWinner(game11SWinner, game12SWinner, trainedModel)

game15SWinner = findWinner(game13SWinner, game14SWinner, trainedModel)

# MidWest
game1MWinner = findWinner("North Carolina", "Iona", trainedModel)
game2MWinner = findWinner("Utah St", "Washington", trainedModel)
game3MWinner = findWinner("Auburn", "New Mexico St", trainedModel)
game4MWinner = findWinner("Kansas", "Northeastern", trainedModel)
game5MWinner = findWinner("Iowa St", "Ohio St", trainedModel)
game6MWinner = findWinner("Houston", "Georgia St", trainedModel)
game7MWinner = findWinner("Wofford", "Seton Hall", trainedModel)
game8MWinner = findWinner("Kentucky", "Abilene Chr", trainedModel)

game9MWinner = findWinner(game1MWinner, game2MWinner, trainedModel)
game10MWinner = findWinner(game3MWinner, game4MWinner, trainedModel)
game11MWinner = findWinner(game5MWinner, game6MWinner, trainedModel)
game12MWinner = findWinner(game7MWinner, game8MWinner, trainedModel)

game13MWinner = findWinner(game9MWinner, game10MWinner, trainedModel)
game14MWinner = findWinner(game11MWinner, game12MWinner, trainedModel)

game15MWinner = findWinner(game13MWinner, game14MWinner, trainedModel)

# Final Four
FF1Winner = findWinner(game15EWinner, game15WWinner, trainedModel)
FF2Winner = findWinner(game15SWinner, game15MWinner, trainedModel)

#Final
FWinner = findWinner(FF1Winner, FF2Winner, trainedModel)

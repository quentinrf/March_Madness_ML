import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

def preprocess():
    data = pd.read_csv("../Relevant_Data/final.csv")
    reduced = data.loc[:, np.isin(data.columns, ['Season', 'Team0', 'Team1'], invert=True)]
    reduced = reduced.sample(reduced.shape[0], random_state=0).reset_index(drop=True)
    nan_cols = list(reduced.isnull().any().index[reduced.isnull().any()])
    reduced = reduced.loc[:, np.isin(reduced.columns, nan_cols, invert=True)]

    X = reduced.loc[:, reduced.columns != "Winner"]
    y = pd.DataFrame(reduced.loc[:, "Winner"])

    X_train = X.loc[0:39999, :] # 80% ish
    y_train = y.loc[0:39999, :]
    X_test = X.loc[40000:, :] # 20% ish
    y_test = y.loc[40000:, :]

    stddev = X_train.std()
    mean = X_train.mean()
    X_train = (X_train - mean)/stddev
    X_test = (X_test - mean)/stddev

    pca = PCA(0.99)
    pca.fit(X_train)
    X_train = pd.DataFrame(pca.transform(X_train))
    X_test = pd.DataFrame(pca.transform(X_test))

    X_train.to_csv("X_train.csv", index=False)
    X_test.to_csv("X_test.csv", index=False)
    y_train.to_csv("y_train.csv", index=False)
    y_test.to_csv("y_test.csv", index=False)

    return nan_cols, mean, stddev, pca



def logistic_regression():
    X_train = pd.read_csv("X_train.csv")
    y_train = pd.read_csv("y_train.csv")

    logr = LogisticRegression()
    logr.fit(X_train, y_train)
    return logr

def random_forest():
    X_train = pd.read_csv("X_train.csv")
    y_train = pd.read_csv("y_train.csv")

    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    return rf

def decision_tree():
    X_train = pd.read_csv("X_train.csv")
    y_train = pd.read_csv("y_train.csv")

    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    return dt

def knn():
    X_train = pd.read_csv("X_train.csv")
    y_train = pd.read_csv("y_train.csv")

    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    return knn


def accuracy(model):
    X_test = pd.read_csv("X_test.csv")
    y_test = pd.read_csv("y_test.csv")

    score = model.score(X_test, y_test)
    return score

def predict(x_vect, mean, stddev, pca, model):
    x = (x_vect - mean) / stddev
    pca.transform(x)
    y = model.predict(x)
    return y


def getTeamStats(Team1, Team2, nan_cols, mean, stddev, pca, model):
    team1_stats = list()
    team2_stats = list()
    data = pd.read_csv("../Relevant_Data/mergedStats_2019.csv")

    print(nan_cols)
    list(nan_cols) + ["School", "Season"]

    t1 = data.loc[data["School"] == Team1, np.isin(data.columns, list(nan_cols) + ["School", "Season"], invert=True)]
    t2 = data.loc[data["School"] == Team2, np.isin(data.columns, list(nan_cols) + ["School", "Season"], invert=True)]
    print(t1)
    print(t2)

    #for row,
    team1_stats = list(t1.values)
    team2_stats = list(t2.values)

    #file = open("teamStats.txt", "w+")
    # for element in team1_stats:
    #     file.write(str(element) + "\n")
    x_vect = np.asarray(list(team1_stats[0]) + list(team2_stats[0]))

    predict(x_vect, mean, stddev, pca, model)
    #print(team1_stats)
    #print(team2_stats)




def calcWinner(mean, stddev, pca, model):
    ######## BRACKET #########
    # East
    eastList = []
    game1EWinner = getTeamStats("Duke", "North Dakota", nan_cols, mean, stddev, pca, model)
    eastList.append(game1EWinner)
    game2EWinner = getTeamStats("VA Commonwealth", "UCF", nan_cols, mean, stddev, pca, model)
    eastList.append(game2EWinner)
    game3EWinner = getTeamStats("Mississippi St", "Liberty", nan_cols, mean, stddev, pca, model)
    eastList.append(game3EWinner)
    game4EWinner = getTeamStats("Virginia Tech", "St Louis", nan_cols, mean, stddev, pca, model)
    eastList.append(game4EWinner)
    game5EWinner = getTeamStats("Maryland", "Belmont", nan_cols, mean, stddev, pca, model)
    eastList.append(game5EWinner)
    game6EWinner = getTeamStats("LSU", "Yale", nan_cols, mean, stddev, pca, model)
    eastList.append(game6EWinner)
    game7EWinner = getTeamStats("Louisville", "Minnesota", nan_cols, mean, stddev, pca, model)
    eastList.append(game7EWinner)
    game8EWinner = getTeamStats("Michigan St", "Bradley", nan_cols, mean, stddev, pca, model)
    eastList.append(game8EWinner)

    game9EWinner = getTeamStats(game1EWinner, game2EWinner, nan_cols, mean, stddev, pca, model)
    eastList.append(game9EWinner)
    game10EWinner = getTeamStats(game3EWinner, game4EWinner, nan_cols, mean, stddev, pca, model)
    eastList.append(game10EWinner)
    game11EWinner = getTeamStats(game5EWinner, game6EWinner, nan_cols, mean, stddev, pca, model)
    eastList.append(game11EWinner)
    game12EWinner = getTeamStats(game7EWinner, game8EWinner, nan_cols, mean, stddev, pca, model)
    eastList.append(game12EWinner)

    game13EWinner = getTeamStats(game9EWinner, game10EWinner, nan_cols, mean, stddev, pca, model)
    eastList.append(game13EWinner)
    game14EWinner = getTeamStats(game11EWinner, game12EWinner, nan_cols, mean, stddev, pca, model)
    eastList.append(game14EWinner)

    game15EWinner = getTeamStats(game13EWinner, game14EWinner, nan_cols, mean, stddev, pca, model)
    eastList.append(game15EWinner)

    print("East Bracket:\n")
    for game in eastList:
        print("Result of game: ", game, "/n")

    # West
    westList = []
    game1WWinner = getTeamStats("Gonzaga", "F Dickinson", nan_cols, mean, stddev, pca, model)
    westList.append(game1WWinner)
    game2WWinner = getTeamStats("Syracuse", "Baylor", nan_cols, mean, stddev, pca, model)
    westList.append(game2WWinner)
    game3WWinner = getTeamStats("Marquette", "Murray St", nan_cols, mean, stddev, pca, model)
    westList.append(game3WWinner)
    game4WWinner = getTeamStats("Florida St", "Vermont", nan_cols, mean, stddev, pca, model)
    westList.append(game4WWinner)
    game5WWinner = getTeamStats("Buffalo", "Arizona St", nan_cols, mean, stddev, pca, model)
    westList.append(game5WWinner)
    game6WWinner = getTeamStats("Texas Tech", "N Kentucky", nan_cols, mean, stddev, pca, model)
    westList.append(game6WWinner)
    game7WWinner = getTeamStats("Nevada", "Florida", nan_cols, mean, stddev, pca, model)
    westList.append(game7WWinner)
    game8WWinner = getTeamStats("Michigan", "Montana", nan_cols, mean, stddev, pca, model)
    westList.append(game8WWinner)
    game9WWinner = getTeamStats(game1WWinner, game2WWinner, nan_cols, mean, stddev, pca, model)
    westList.append(game9WWinner)
    game10WWinner = getTeamStats(game3WWinner, game4WWinner, nan_cols, mean, stddev, pca, model)
    westList.append(game10WWinner)
    game11WWinner = getTeamStats(game5WWinner, game6WWinner, nan_cols, mean, stddev, pca, model)
    westList.append(game11WWinner)
    game12WWinner = getTeamStats(game7WWinner, game8WWinner, nan_cols, mean, stddev, pca, model)
    westList.append(game12WWinner)

    game13WWinner = getTeamStats(game9WWinner, game10WWinner, nan_cols, mean, stddev, pca, model)
    westList.append(game13WWinner)
    game14WWinner = getTeamStats(game11WWinner, game12WWinner, nan_cols, mean, stddev, pca, model)
    westList.append(game14WWinner)

    game15WWinner = getTeamStats(game13WWinner, game14WWinner, nan_cols, mean, stddev, pca, model)
    westList.append(game15WWinner)

    print("West Bracket:\n")
    for game in westList:
        print("Result of game: ", game, "/n")

    # South
    southList = []
    game1SWinner = getTeamStats("Virginia", "Gardner Webb", nan_cols, mean, stddev, pca, model)
    southList.append(game1SWinner)
    game2SWinner = getTeamStats("Mississippi", "Oklahoma", nan_cols, mean, stddev, pca, model)
    southList.append(game2SWinner)
    game3SWinner = getTeamStats("Wisconsin", "Oregon", nan_cols, mean, stddev, pca, model)
    southList.append(game3SWinner)
    game4SWinner = getTeamStats("Kansas St", "UC Irvine", nan_cols, mean, stddev, pca, model)
    southList.append(game4SWinner)
    game5SWinner = getTeamStats("Villanova", "St Mary's CA", nan_cols, mean, stddev, pca, model)
    southList.append(game5SWinner)
    game6SWinner = getTeamStats("Purdue", "Old Dominion", nan_cols, mean, stddev, pca, model)
    southList.append(game6SWinner)
    game7SWinner = getTeamStats("Cincinati", "Iowa", nan_cols, mean, stddev, pca, model)
    southList.append(game7SWinner)
    game8SWinner = getTeamStats("Tennessee", "Colgate", nan_cols, mean, stddev, pca, model)
    southList.append(game8SWinner)

    game9SWinner = getTeamStats(game1SWinner, game2SWinner, nan_cols, mean, stddev, pca, model)
    southList.append(game9SWinner)
    game10SWinner = getTeamStats(game3SWinner, game4SWinner, nan_cols, mean, stddev, pca, model)
    southList.append(game10SWinner)
    game11SWinner = getTeamStats(game5SWinner, game6SWinner, nan_cols, mean, stddev, pca, model)
    southList.append(game11SWinner)
    game12SWinner = getTeamStats(game7SWinner, game8SWinner, nan_cols, mean, stddev, pca, model)
    southList.append(game12SWinner)

    game13SWinner = getTeamStats(game9SWinner, game10SWinner, nan_cols, mean, stddev, pca, model)
    southList.append(game13SWinner)
    game14SWinner = getTeamStats(game11SWinner, game12SWinner, nan_cols, mean, stddev, pca, model)
    southList.append(game14SWinner)

    game15SWinner = getTeamStats(game13SWinner, game14SWinner, nan_cols, mean, stddev, pca, model)
    southList.append(game15SWinner)

    print("South Bracket:\n")
    for game in southList:
        print("Result of game: ", game, "/n")

    # MidWest
    midList = []
    game1MWinner = getTeamStats("North Carolina", "Iona", nan_cols, mean, stddev, pca, model)
    midList.append(game1MWinner)
    game2MWinner = getTeamStats("Utah St", "Washington", nan_cols, mean, stddev, pca, model)
    midList.append(game2MWinner)
    game3MWinner = getTeamStats("Auburn", "New Mexico St", nan_cols, mean, stddev, pca, model)
    midList.append(game3MWinner)
    game4MWinner = getTeamStats("Kansas", "Northeastern", nan_cols, mean, stddev, pca, model)
    midList.append(game4MWinner)
    game5MWinner = getTeamStats("Iowa St", "Ohio St", nan_cols, mean, stddev, pca, model)
    midList.append(game5MWinner)
    game6MWinner = getTeamStats("Houston", "Georgia St", nan_cols, mean, stddev, pca, model)
    midList.append(game6MWinner)
    game7MWinner = getTeamStats("Wofford", "Seton Hall", nan_cols, mean, stddev, pca, model)
    midList.append(game7MWinner)
    game8MWinner = getTeamStats("Kentucky", "Abilene Chr", nan_cols, mean, stddev, pca, model)
    midList.append(game8MWinner)

    game9MWinner = getTeamStats(game1MWinner, game2MWinner, nan_cols, mean, stddev, pca, model)
    midList.append(game9MWinner)
    game10MWinner = getTeamStats(game3MWinner, game4MWinner, nan_cols, mean, stddev, pca, model)
    midList.append(game10MWinner)
    game11MWinner = getTeamStats(game5MWinner, game6MWinner, nan_cols, mean, stddev, pca, model)
    midList.append(game11MWinner)
    game12MWinner = getTeamStats(game7MWinner, game8MWinner, nan_cols, mean, stddev, pca, model)
    midList.append(game12MWinner)

    game13MWinner = getTeamStats(game9MWinner, game10MWinner, nan_cols, mean, stddev, pca, model)
    midList.append(game13MWinner)
    game14MWinner = getTeamStats(game11MWinner, game12MWinner, nan_cols, mean, stddev, pca, model)
    midList.append(game14MWinner)

    game15MWinner = getTeamStats(game13MWinner, game14MWinner, nan_cols, mean, stddev, pca, model)
    midList.append(game15MWinner)

    print("MidWest Bracket:\n")
    for game in midList:
        print("Result of game: ", game, "/n")

    # Final Four
    FF1Winner = getTeamStats(game15EWinner, game15WWinner, nan_cols, mean, stddev, pca, model)
    FF2Winner = getTeamStats(game15SWinner, game15MWinner, nan_cols, mean, stddev, pca, model)

    print("Final Four 1 Results:", FF1Winner, "/n")
    print("Final Four 2 Results:", FF2Winner, "/n")

    #Final
    FWinner = getTeamStats(FF1Winner, FF2Winner, nan_cols, mean, stddev, pca, model)

    print("Grand Champion:", FWinner)






nan_cols, mean, stddev, pca = preprocess()
logr = logistic_regression()

print(getTeamStats("North Carolina", "Iona", nan_cols, mean, stddev, pca, logr))



# calcWinner(mean, stddev, pca, logr)

# rf = random_forest()
# dt = decision_tree()
# knn = knn()

# print(accuracy(logr))
# print(accuracy(rf))
# print(accuracy(dt))
# print(accuracy(knn))


# print(predict(x_vect, mean, stddev, logr))





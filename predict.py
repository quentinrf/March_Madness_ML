

def calcWinner():
    ######## BRACKET #########
    # East
    eastList = []
    game1EWinner = findWinner("Duke", "North Dakota", trainedModel)
    eastList.append(game1EWinner)
    game2EWinner = findWinner("VA Commonwealth", "UCF", trainedModel)
    eastList.append(game2EWinner)
    game3EWinner = findWinner("Mississippi St", "Liberty", trainedModel)
    eastList.append(game3EWinner)
    game4EWinner = findWinner("Virginia Tech", "St Louis", trainedModel)
    eastList.append(game4EWinner)
    game5EWinner = findWinner("Maryland", "Belmont", trainedModel)
    eastList.append(game5EWinner)
    game6EWinner = findWinner("LSU", "Yale", trainedModel)
    eastList.append(game6EWinner)
    game7EWinner = findWinner("Louisville", "Minnesota", trainedModel)
    eastList.append(game7EWinner)
    game8EWinner = findWinner("Michigan St", "Bradley", trainedModel)
    eastList.append(game8EWinner)

    game9EWinner = findWinner(game1EWinner, game2EWinner, trainedModel)
    eastList.append(game9EWinner)
    game10EWinner = findWinner(game3EWinner, game4EWinner, trainedModel)
    eastList.append(game10EWinner)
    game11EWinner = findWinner(game5EWinner, game6EWinner, trainedModel)
    eastList.append(game11EWinner)
    game12EWinner = findWinner(game7EWinner, game8EWinner, trainedModel)
    eastList.append(game12EWinner)

    game13EWinner = findWinner(game9EWinner, game10EWinner, trainedModel)
    eastList.append(game13EWinner)
    game14EWinner = findWinner(game11EWinner, game12EWinner, trainedModel)
    eastList.append(game14EWinner)

    game15EWinner = findWinner(game13EWinner, game14EWinner, trainedModel)
    eastList.append(game15EWinner)

    print("East Bracket:\n")
    for game in eastList:
        print("Result of game: ", game, "/n")

    # West
    westList = []
    game1WWinner = findWinner("Gonzaga", "F Dickinson", trainedModel)
    westList.append(game1WWinner)
    game2WWinner = findWinner("Syracuse", "Baylor", trainedModel)
    westList.append(game2WWinner)
    game3WWinner = findWinner("Marquette", "Murray St", trainedModel)
    westList.append(game3WWinner)
    game4WWinner = findWinner("Florida St", "Vermont", trainedModel)
    westList.append(game4WWinner)
    game5WWinner = findWinner("Buffalo", "Arizona St", trainedModel)
    westList.append(game5WWinner)
    game6WWinner = findWinner("Texas Tech", "N Kentucky", trainedModel)
    westList.append(game6WWinner)
    game7WWinner = findWinner("Nevada", "Florida", trainedModel)
    westList.append(game7WWinner)
    game8WWinner = findWinner("Michigan", "Montana", trainedModel)
    westList.append(game8WWinner)
    game9WWinner = findWinner(game1WWinner, game2WWinner, trainedModel)
    westList.append(game9WWinner)
    game10WWinner = findWinner(game3WWinner, game4WWinner, trainedModel)
    westList.append(game10WWinner)
    game11WWinner = findWinner(game5WWinner, game6WWinner, trainedModel)
    westList.append(game11WWinner)
    game12WWinner = findWinner(game7WWinner, game8WWinner, trainedModel)
    westList.append(game12WWinner)

    game13WWinner = findWinner(game9WWinner, game10WWinner, trainedModel)
    westList.append(game13WWinner)
    game14WWinner = findWinner(game11WWinner, game12WWinner, trainedModel)
    westList.append(game14WWinner)

    game15WWinner = findWinner(game13WWinner, game14WWinner, trainedModel)
    westList.append(game15WWinner)

    print("West Bracket:\n")
    for game in westList:
        print("Result of game: ", game, "/n")

    # South
    southList = []
    game1SWinner = findWinner("Virginia", "Gardner Webb", trainedModel)
    southList.append(game1SWinner)
    game2SWinner = findWinner("Mississippi", "Oklahoma", trainedModel)
    southList.append(game2SWinner)
    game3SWinner = findWinner("Wisconsin", "Oregon", trainedModel)
    southList.append(game3SWinner)
    game4SWinner = findWinner("Kansas St", "UC Irvine", trainedModel)
    southList.append(game4SWinner)
    game5SWinner = findWinner("Villanova", "St Mary's CA", trainedModel)
    southList.append(game5SWinner)
    game6SWinner = findWinner("Purdue", "Old Dominion", trainedModel)
    southList.append(game6SWinner)
    game7SWinner = findWinner("Cincinati", "Iowa", trainedModel)
    southList.append(game7SWinner)
    game8SWinner = findWinner("Tennessee", "Colgate", trainedModel)
    southList.append(game8SWinner)

    game9SWinner = findWinner(game1SWinner, game2SWinner, trainedModel)
    southList.append(game9SWinner)
    game10SWinner = findWinner(game3SWinner, game4SWinner, trainedModel)
    southList.append(game10SWinner)
    game11SWinner = findWinner(game5SWinner, game6SWinner, trainedModel)
    southList.append(game11SWinner)
    game12SWinner = findWinner(game7SWinner, game8SWinner, trainedModel)
    southList.append(game12SWinner)

    game13SWinner = findWinner(game9SWinner, game10SWinner, trainedModel)
    southList.append(game13SWinner)
    game14SWinner = findWinner(game11SWinner, game12SWinner, trainedModel)
    southList.append(game14SWinner)

    game15SWinner = findWinner(game13SWinner, game14SWinner, trainedModel)
    southList.append(game15SWinner)

    print("South Bracket:\n")
    for game in southList:
        print("Result of game: ", game, "/n")

    # MidWest
    midList = []
    game1MWinner = findWinner("North Carolina", "Iona", trainedModel)
    midList.append(game1MWinner)
    game2MWinner = findWinner("Utah St", "Washington", trainedModel)
    midList.append(game2MWinner)
    game3MWinner = findWinner("Auburn", "New Mexico St", trainedModel)
    midList.append(game3MWinner)
    game4MWinner = findWinner("Kansas", "Northeastern", trainedModel)
    midList.append(game4MWinner)
    game5MWinner = findWinner("Iowa St", "Ohio St", trainedModel)
    midList.append(game5MWinner)
    game6MWinner = findWinner("Houston", "Georgia St", trainedModel)
    midList.append(game6MWinner)
    game7MWinner = findWinner("Wofford", "Seton Hall", trainedModel)
    midList.append(game7MWinner)
    game8MWinner = findWinner("Kentucky", "Abilene Chr", trainedModel)
    midList.append(game8MWinner)

    game9MWinner = findWinner(game1MWinner, game2MWinner, trainedModel)
    midList.append(game9MWinner)
    game10MWinner = findWinner(game3MWinner, game4MWinner, trainedModel)
    midList.append(game10MWinner)
    game11MWinner = findWinner(game5MWinner, game6MWinner, trainedModel)
    midList.append(game11MWinner)
    game12MWinner = findWinner(game7MWinner, game8MWinner, trainedModel)
    midList.append(game12MWinner)

    game13MWinner = findWinner(game9MWinner, game10MWinner, trainedModel)
    midList.append(game13MWinner)
    game14MWinner = findWinner(game11MWinner, game12MWinner, trainedModel)
    midList.append(game14MWinner)

    game15MWinner = findWinner(game13MWinner, game14MWinner, trainedModel)
    midList.append(game15MWinner)

    print("MidWest Bracket:\n")
    for game in midList:
        print("Result of game: ", game, "/n")

    # Final Four
    FF1Winner = findWinner(game15EWinner, game15WWinner, trainedModel)
    FF2Winner = findWinner(game15SWinner, game15MWinner, trainedModel)

    print("Final Four 1 Results:", FF1Winner, "/n")
    print("Final Four 2 Results:", FF2Winner, "/n")

    #Final
    FWinner = findWinner(FF1Winner, FF2Winner, trainedModel)

    print("Grand Champion:", FWinner)

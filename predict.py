def calcWinner():
    ######## BRACKET #########
    # East
    eastList = []
    game1EWinner = getTeamStats("Duke", "North Dakota", trainedModel)
    eastList.append(game1EWinner)
    game2EWinner = getTeamStats("VA Commonwealth", "UCF", trainedModel)
    eastList.append(game2EWinner)
    game3EWinner = getTeamStats("Mississippi St", "Liberty", trainedModel)
    eastList.append(game3EWinner)
    game4EWinner = getTeamStats("Virginia Tech", "St Louis", trainedModel)
    eastList.append(game4EWinner)
    game5EWinner = getTeamStats("Maryland", "Belmont", trainedModel)
    eastList.append(game5EWinner)
    game6EWinner = getTeamStats("LSU", "Yale", trainedModel)
    eastList.append(game6EWinner)
    game7EWinner = getTeamStats("Louisville", "Minnesota", trainedModel)
    eastList.append(game7EWinner)
    game8EWinner = getTeamStats("Michigan St", "Bradley", trainedModel)
    eastList.append(game8EWinner)

    game9EWinner = getTeamStats(game1EWinner, game2EWinner, trainedModel)
    eastList.append(game9EWinner)
    game10EWinner = getTeamStats(game3EWinner, game4EWinner, trainedModel)
    eastList.append(game10EWinner)
    game11EWinner = getTeamStats(game5EWinner, game6EWinner, trainedModel)
    eastList.append(game11EWinner)
    game12EWinner = getTeamStats(game7EWinner, game8EWinner, trainedModel)
    eastList.append(game12EWinner)

    game13EWinner = getTeamStats(game9EWinner, game10EWinner, trainedModel)
    eastList.append(game13EWinner)
    game14EWinner = getTeamStats(game11EWinner, game12EWinner, trainedModel)
    eastList.append(game14EWinner)

    game15EWinner = getTeamStats(game13EWinner, game14EWinner, trainedModel)
    eastList.append(game15EWinner)

    print("East Bracket:\n")
    for game in eastList:
        print("Result of game: ", game, "/n")

    # West
    westList = []
    game1WWinner = getTeamStats("Gonzaga", "F Dickinson", trainedModel)
    westList.append(game1WWinner)
    game2WWinner = getTeamStats("Syracuse", "Baylor", trainedModel)
    westList.append(game2WWinner)
    game3WWinner = getTeamStats("Marquette", "Murray St", trainedModel)
    westList.append(game3WWinner)
    game4WWinner = getTeamStats("Florida St", "Vermont", trainedModel)
    westList.append(game4WWinner)
    game5WWinner = getTeamStats("Buffalo", "Arizona St", trainedModel)
    westList.append(game5WWinner)
    game6WWinner = getTeamStats("Texas Tech", "N Kentucky", trainedModel)
    westList.append(game6WWinner)
    game7WWinner = getTeamStats("Nevada", "Florida", trainedModel)
    westList.append(game7WWinner)
    game8WWinner = getTeamStats("Michigan", "Montana", trainedModel)
    westList.append(game8WWinner)
    game9WWinner = getTeamStats(game1WWinner, game2WWinner, trainedModel)
    westList.append(game9WWinner)
    game10WWinner = getTeamStats(game3WWinner, game4WWinner, trainedModel)
    westList.append(game10WWinner)
    game11WWinner = getTeamStats(game5WWinner, game6WWinner, trainedModel)
    westList.append(game11WWinner)
    game12WWinner = getTeamStats(game7WWinner, game8WWinner, trainedModel)
    westList.append(game12WWinner)

    game13WWinner = getTeamStats(game9WWinner, game10WWinner, trainedModel)
    westList.append(game13WWinner)
    game14WWinner = getTeamStats(game11WWinner, game12WWinner, trainedModel)
    westList.append(game14WWinner)

    game15WWinner = getTeamStats(game13WWinner, game14WWinner, trainedModel)
    westList.append(game15WWinner)

    print("West Bracket:\n")
    for game in westList:
        print("Result of game: ", game, "/n")

    # South
    southList = []
    game1SWinner = getTeamStats("Virginia", "Gardner Webb", trainedModel)
    southList.append(game1SWinner)
    game2SWinner = getTeamStats("Mississippi", "Oklahoma", trainedModel)
    southList.append(game2SWinner)
    game3SWinner = getTeamStats("Wisconsin", "Oregon", trainedModel)
    southList.append(game3SWinner)
    game4SWinner = getTeamStats("Kansas St", "UC Irvine", trainedModel)
    southList.append(game4SWinner)
    game5SWinner = getTeamStats("Villanova", "St Mary's CA", trainedModel)
    southList.append(game5SWinner)
    game6SWinner = getTeamStats("Purdue", "Old Dominion", trainedModel)
    southList.append(game6SWinner)
    game7SWinner = getTeamStats("Cincinati", "Iowa", trainedModel)
    southList.append(game7SWinner)
    game8SWinner = getTeamStats("Tennessee", "Colgate", trainedModel)
    southList.append(game8SWinner)

    game9SWinner = getTeamStats(game1SWinner, game2SWinner, trainedModel)
    southList.append(game9SWinner)
    game10SWinner = getTeamStats(game3SWinner, game4SWinner, trainedModel)
    southList.append(game10SWinner)
    game11SWinner = getTeamStats(game5SWinner, game6SWinner, trainedModel)
    southList.append(game11SWinner)
    game12SWinner = getTeamStats(game7SWinner, game8SWinner, trainedModel)
    southList.append(game12SWinner)

    game13SWinner = getTeamStats(game9SWinner, game10SWinner, trainedModel)
    southList.append(game13SWinner)
    game14SWinner = getTeamStats(game11SWinner, game12SWinner, trainedModel)
    southList.append(game14SWinner)

    game15SWinner = getTeamStats(game13SWinner, game14SWinner, trainedModel)
    southList.append(game15SWinner)

    print("South Bracket:\n")
    for game in southList:
        print("Result of game: ", game, "/n")

    # MidWest
    midList = []
    game1MWinner = getTeamStats("North Carolina", "Iona", trainedModel)
    midList.append(game1MWinner)
    game2MWinner = getTeamStats("Utah St", "Washington", trainedModel)
    midList.append(game2MWinner)
    game3MWinner = getTeamStats("Auburn", "New Mexico St", trainedModel)
    midList.append(game3MWinner)
    game4MWinner = getTeamStats("Kansas", "Northeastern", trainedModel)
    midList.append(game4MWinner)
    game5MWinner = getTeamStats("Iowa St", "Ohio St", trainedModel)
    midList.append(game5MWinner)
    game6MWinner = getTeamStats("Houston", "Georgia St", trainedModel)
    midList.append(game6MWinner)
    game7MWinner = getTeamStats("Wofford", "Seton Hall", trainedModel)
    midList.append(game7MWinner)
    game8MWinner = getTeamStats("Kentucky", "Abilene Chr", trainedModel)
    midList.append(game8MWinner)

    game9MWinner = getTeamStats(game1MWinner, game2MWinner, trainedModel)
    midList.append(game9MWinner)
    game10MWinner = getTeamStats(game3MWinner, game4MWinner, trainedModel)
    midList.append(game10MWinner)
    game11MWinner = getTeamStats(game5MWinner, game6MWinner, trainedModel)
    midList.append(game11MWinner)
    game12MWinner = getTeamStats(game7MWinner, game8MWinner, trainedModel)
    midList.append(game12MWinner)

    game13MWinner = getTeamStats(game9MWinner, game10MWinner, trainedModel)
    midList.append(game13MWinner)
    game14MWinner = getTeamStats(game11MWinner, game12MWinner, trainedModel)
    midList.append(game14MWinner)

    game15MWinner = getTeamStats(game13MWinner, game14MWinner, trainedModel)
    midList.append(game15MWinner)

    print("MidWest Bracket:\n")
    for game in midList:
        print("Result of game: ", game, "/n")

    # Final Four
    FF1Winner = getTeamStats(game15EWinner, game15WWinner, trainedModel)
    FF2Winner = getTeamStats(game15SWinner, game15MWinner, trainedModel)

    print("Final Four 1 Results:", FF1Winner, "/n")
    print("Final Four 2 Results:", FF2Winner, "/n")

    #Final
    FWinner = getTeamStats(FF1Winner, FF2Winner, trainedModel)

    print("Grand Champion:", FWinner)

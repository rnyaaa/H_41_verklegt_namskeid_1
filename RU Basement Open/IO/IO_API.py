class IO_API:

    def getAllPlayers():
        playerstream = playerIO.loadPlayersFile()
        for line in playerstream:
            print(line)
        return playerstream

    def getAllTeams():
        teamstream = teamIO.loadTeamsFile()
        return teamstream

    def getAllGames():
        gamestream = gameIO.loadGamesFile()
        return gamestream

    def getAllTournaments():
        tournamentstream = tournamentIO.loadTournamentFile()
        return tournamentstream

    def getResults():
        resultstream = resultsIO.loadResultsFile()
        return resultstream

    def updatePlayers(playerupdate):
        playerIO.storePlayersFile(playerupdate)

    def updateTeams(teamupdate):
        teamIO.storeTeamsFile(teamupdate)

    def updateGames(gameupdate):
        gameIO.storeGamesFile(gameupdate)

    def updateTournaments(tournamentupdate):
        tournamentIO.storeTournamentFile(tournamentupdate)

    def updateResults(newresults, resultsID):
        resultsIO.storeResultsFile(newresults,resultsID)

class playerIO:
    def loadPlayersFile():
        playerstream = open("/home/ronja/Downloads/Pilukast/models/players.csv", "r")
        return playerstream

    def storePlayersFile(playerupdate):
        append_player = open("/home/ronja/Downloads/Pilukast/models/players.csv", "a")
        append_player.write(playerupdate)
        append_player.close()

class teamIO:
    def loadTeamsFile():
        teamstream = open("/models/teams.csv", "r")
        return teamstream

    def storeTeamsFile(teamupdate):
        append_teams = open("models/teams.csv", "a")
        append_teams.write(teamupdate)
        append_teams.close()

class gameIO:
    def loadGamesFile():
        gamestream = open("/models/games.csv", "r")
        return gamestream

    def storeGamesFile(gamesupdate):
        append_games = open("models/games.csv", "a")
        append_games.write(gamesupdate)
        append_games.close()

class tournamentIO:
    def loadTournamentFile():
        tournamentstream = open("/models/tournaments.csv", "r")
        return tournamentstream

    def storeTournamentFile(tournamentupdate):
        append_tournament = open("models/teams.csv", "a")
        append_tournament.write(tournamentupdate)
        append_tournament.close()

class resultsIO:
    def loadResultsFile():
        resultstream = open("/models/results.csv", "r")
        return resultstream

    def storeResultsFile(newresults, resultsID):
        create_new_results = open(resultsID.csv, "x")
        create_new_results.close()
        write_new_results = open(resultsID.csv, "w")
        write_new_results.write(newresults)
        write_new_results.close()

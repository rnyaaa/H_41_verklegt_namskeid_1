class IO_API():
    def getAllPlayers():
        playerstream = playerIO.loadPlayersFile()
        return playerstream

    def getAllTeams():
        teamstream = teamIO.loadTeamsFile()
        return teamstream

    def getAllGames():
        gamestream = gameIO.loadGamesFile()
        return gamestream

    def getAllTournaments():
        tournamentstream = tournamentIO.loadGamesFile()
        return tournamentstream

    def getResults():
        resultstream = resultsIO.loadResultsFile()
        return resultstream

    def updatePlayers():
        raise NotImplementedError

    def updateTeams():
        raise NotImplementedError

    def updateGames():
        raise NotImplementedError

    def updateTournaments():
        raise NotImplementedError


class playerIO():
    def loadPlayersFile():
        playerstream = open("/models/players.csv", "r")
        return playerstream

    def storePlayersFile():
        raise NotImplementedError

class teamIO():
    def loadTeamsFile():
        teamstream = open("/models/teams.csv", "r")
        return teamstream

    def storeTeamsFile():
        raise NotImplementedError

class gameIO():
    def loadGamesFile():
        gamestream = open("/models/games.csv", "r")
        return gamestream

    def storeGamesFile():
        raise NotImplementedError

class tournamentIO():
    def loadTournamentFile():
        tournamentstream = open("/models/tournaments.csv", "r")
        return tournamentstream

    def storeTournamentFile():
        raise NotImplementedError

class resultsIO():
    def loadResultsFile():
        resultstream = open("/models/results.csv", "r")
        return resultstream

    def storeResultsFile():
        raise NotImplementedError

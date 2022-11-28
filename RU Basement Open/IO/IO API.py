class IO_API():
    def getAllPlayers():
        raise NotImplementedError

    def getAllTeams():
        raise NotImplementedError

    def getAllGames():
        raise NotImplementedError

    def getAllTournaments():
        raise NotImplementedError

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
        raise NotImplementedError

    def storePlayersFile():
        raise NotImplementedError

class teamIO():
    def loadTeamsFile():
        raise NotImplementedError

    def storeTeamsFile():
        raise NotImplementedError

class gameIO():
    def loadGamesFile():
        raise NotImplementedError

    def storeGamesFile():
        raise NotImplementedError

class tournamentIO():
    def loadTournamentFile():
        raise NotImplementedError

    def storeTournamentFile():
        raise NotImplementedError

class resultsIO():
    def loadResultsFile():
        raise NotImplementedError

    def storeResultsFile():
        raise NotImplementedError

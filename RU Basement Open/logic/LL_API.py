
from IO_API import IO_API

class LL_API():
    def getPlayers(self):
        playerstream = IO_API.getAllPlayers()
        return playerstream

    def getTeams():
        teamstream = IO_API.getAllTeams()
        return teamstream

    def getGames():
        gamestream = IO_API.getAllGames()
        return gamestream

    def getTournament():
        tournamentstream = IO_API.getAllTournaments()
        return tournamentstream

    def getResults():
        resultstream = IO_API.getResults()
        return resultstream

    def getPlayerScore(playername = str):
        for line in playerstream.split(","):
            if line[0] == playername:
                scores = [line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17], line[18], line[19]]
        return scores

    def getPlayerScoreByDate():
        raise NotImplementedError

    def getPlayerSortQP():
        raise NotImplementedError

    def getPlayerSortInshorts():
        raise NotImplementedError

    def getPlayerSortOutshot():
        raise NotImplementedError

    def getTournamentScores():
        raise NotImplementedError

    def getTournamentDates():
        raise NotImplementedError

    def getGamesFinished():
        raise NotImplementedError

    def getUpcomingGames():
        raise NotImplementedError

    def addTeam():
        IO_API.updateTeams(newteam=str)

    def addGame():
        IO_API.updateGames(gamesupdate=str)
        
    def addPlayer():

    def changeResults():
        raise NotImplementedError

    def changeDate():
        raise NotImplementedError

    def updatePlayers():
        IO_API.updatePlayers(playerupdate)

    def updateTeams():
        IO_API.updateTeams(teamsupdate=str)

    def updateGames():
        IO_API.updateGames(gamesupdate=str)

    def updateTournament():
        IO_API.updateTournaments(tournamentupdate=str)

    def updateResults():
        IO_API.updateResults(newresults=str, resultsID=str)

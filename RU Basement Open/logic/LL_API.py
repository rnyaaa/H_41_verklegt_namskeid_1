from IO.IO_API import IO_API
from logic.PlayersLL import PlayersLL
from logic.ViewerLL import ViewerLL
from logic.TournamentLL import TournamentLL
from logic.ResultsLL import ResultsLL
from logic.GamesLL import GameLL

class LL_API:
    def getPlayers():
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

    def getResults(resultsID):
        resultstream = IO_API.getResults(resultsID)
        return resultstream

    def getPlayerScore(playername = str):
        scores = ViewerLL.getPlayerScore
        return scores

    def getPlayerScoreByDate():
        raise NotImplementedError


    def getTournamentScores():
        tournamentscorelist = ViewerLL.getTournamentScore()
        return tournamentscorelist
                

    def getTournamentDates():
        tournamentdatelist = ViewerLL.getTournamentDates()
        return tournamentdatelist

    def getGamesFinished():
        gamesfinished = ViewerLL.getGameFinished()
        return gamesfinished

    def getUpcomingGames():
        gamesupcoming = ViewerLL.getUpcomingGames()
        return gamesupcoming
        
    def getPlayerList():
        players = ViewerLL.getPlayerList
        return players

    def addTeam(newteam):
        IO_API.updateTeams(newteam=str)
    
    def addTournament(tournamentinfo=str):
        TournamentLL.addTournament(tournamentinfo=str)

    def addGame(gamesupdate):
        IO_API.updateGames(gamesupdate=str)
        
    def addPlayer(playeradd=str):
        PlayersLL.addPlayers(playeradd=str)

    def changeResults():
        raise NotImplementedError

    def changeDate():
        raise NotImplementedError

    def updatePlayers(playerupdate=str):
        IO_API.updatePlayers(playerupdate=str)

    def updateTeams(teamsupdate):
        IO_API.updateTeams(teamsupdate=str)

    def updateGames(gamesupdate):
        IO_API.updateGames(gamesupdate=str)

    def updateTournament(tournamentupdate):
        IO_API.updateTournaments(tournamentupdate=str)

    def updateResults():
        IO_API.updateResults(newresults=str, resultsID=str)

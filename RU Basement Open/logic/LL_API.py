from IO.IO_API import IO_API
from logic.PlayersLL import PlayersLL
from logic.TournamentLL import TournamentLL
from logic.ViewerLL import ViewerLL
from logic.ResultsLL import ResultsLL

PLAYERS = "models/players.csv"
GAMES = "models/teams.csv"
TEAMS = "models/teams.csv"
TOURNAMENTS = "models/tournaments.csv"

class LL_API():
    def __init__(self):
        self.playerll = PlayersLL()
        self.tournamentLL = TournamentLL()
        self.viewerLL = ViewerLL()
        self.resultsLL = ResultsLL()

    def getPlayers(self):
        playersfile = IO_API.getAll(PLAYERS)
        return playersfile

    def getTeams(self):
        teamsfile = IO_API.getAll(TEAMS)
        return teamsfile

    def getGames(self):
        gamesfile = IO_API.getAll(GAMES)
        return gamesfile

    def getTournament(self):
        tournamentsfile = IO_API.getAll(TOURNAMENTS)
        return tournamentsfile

    def getResults(self, resultsID):
        resultstream = IO_API.getResults(resultsID)
        return resultstream

    def getPlayerScore(self, playername = str):
        scores = ViewerLL.getPlayerScore
        return scores

    def getPlayerScoreByDate(self):
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
        #PlayersLL.addPlayers(playeradd=str)
        raise

    def changeResults():
        raise NotImplementedError

    def changeDate():
        raise NotImplementedError

    def updatePlayers(playerupdate=str):
        IO_API.Update(playerupdate=str, PLAYERS)

    def updateTeams(teamsupdate):
        IO_API.Update(teamsupdate=str, TEAMS)

    def updateGames(gamesupdate):
        IO_API.Update(gamesupdate=str, GAMES)

    def updateTournament(tournamentupdate, ):
        IO_API.Update(tournamentupdate=str, TOURNAMENTS)

    def updateResults(newresults, resultsID):
        IO_API.updateResults(newresults=str, resultsID=str)

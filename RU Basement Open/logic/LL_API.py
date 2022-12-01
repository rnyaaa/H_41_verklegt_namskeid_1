from IO.IO_API import IO_API
from logic.PlayersLL import PlayersLL
from logic.TournamentLL import TournamentLL
from logic.ViewerLL import ViewerLL
from logic.ResultsLL import ResultsLL

# verðum að hætta að importa LL_API inn í hina LL klasana, annars fáum við circular import
# Megum bara importa hinum LL klösunum inn í LL_API en ekki öfugt!

PLAYERS = "models/players.csv"
GAMES = "models/teams.csv"
TEAMS = "models/teams.csv"
TOURNAMENTS = "models/tournaments.csv"


class LL_API:

    def __init__(self):
        self.ioapi = IO_API()
        self.playerll = PlayersLL(self.ioapi)
        self.tournamentLL = TournamentLL()
        self.viewerLL = ViewerLL()
        self.resultsLL = ResultsLL()

    def getPlayers(self):
        return self.playerll.get_all_players()

    def createPlayer(self, player):
        return self.playerll.createPlayer(player)

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

    def getPlayerScore(self, playername=str):
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

    # def addPlayer(playeradd=str):
    #    PlayersLL.addPlayers(playeradd=str)
    #    raise

    def changeResults():
        raise NotImplementedError

    def changeDate():
        raise NotImplementedError

    def updatePlayers(playerupdate=list):
        IO_API.Update(PLAYERS, playerupdate=list)

    def updateTeams(teamsupdate=list):
        IO_API.Update(PLAYERS, teamsupdate=list)

    def updateGames(gamesupdate=list):
        IO_API.Update(GAMES, gamesupdate=list)

    def updateTournament(tournamentupdate=list):
        IO_API.Update(TOURNAMENTS, tournamentupdate=list)

    def updateResults(newresults=list, resultsID=str):
        IO_API.updateResults(newresults=list, resultsID=str)

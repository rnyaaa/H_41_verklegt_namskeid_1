from IO.IO_API import IO_API
from models.player import Player
from logic.PlayersLL import PlayersLL
from logic.ResultsLL import ResultsLL
from logic.TeamsLL import TeamsLL
from logic.TournamentLL import TournamentLL
from logic.GamesLL import GamesLL

# verðum að hætta að importa LL_API inn í hina LL klasana, annars fáum við circular import
# Megum bara importa hinum LL klösunum inn í LL_API en ekki öfugt!

PLAYERS = "models/players.csv"
GAMES = "models/teams.csv"
TEAMS = "models/teams.csv"
TOURNAMENTS = "models/tournaments.csv"


class LL_API:

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi
        self.playerLL = PlayersLL(ioapi)
        self.tournamentLL = TournamentLL(ioapi)
        self.teamLL = TeamsLL(ioapi)
        self.resultsLL = ResultsLL(ioapi)
        self.gamesLL = GamesLL(ioapi)

    def getPlayers(self):
        return self.playerLL.get_all_players()

    def createPlayer(self, player: Player):
        self.playerLL.createPlayer(player)

    def getTeams(self):
        return self.teamLL.get_all_teams()

    def getGames(self):
        gamesfile = self.ioapi.getAll(GAMES)
        return gamesfile

    def getTournament(self):
        return self.tournamentLL
        # tournamentsfile = self.ioapi.getAll(TOURNAMENTS)
        # return tournamentsfile

    def getResults(self, resultsID):
        resultstream = self.ioapi.getResults(resultsID)
        return resultstream

    def getPlayerScore(self, playername: str):
        scores = PlayersLL.getPlayerScore(playername)
        return scores

    def getPlayerScoreByDate(self):
        raise NotImplementedError

    def getTournamentScores():
        tournamentscorelist = TournamentLL.getTournamentScore()
        return tournamentscorelist

    def getTournamentDates():
        tournamentdatelist = TournamentLL.getTournamentDates()
        return tournamentdatelist

    def getGamesFinished():
        gamesfinished = GamesLL.getGameFinished()
        return gamesfinished

    def getUpcomingGames():
        gamesupcoming = GamesLL.getUpcomingGames()
        return gamesupcoming

    def getPlayerList():
        players = PlayersLL.getPlayerList
        return players

    def addTeam(self, newteam):
        self.teamLL.addTeams(newteam=str)

    def addTournament(self, tournamentinfo=str):
        self.tournamentLL.addTournament(tournamentinfo=str)

    def addGame(self, gamesupdate):
        self.ioapi.updateGames(gamesupdate=str)

    # def addPlayer(playeradd=str):
    #    PlayersLL.addPlayers(playeradd=str)
    #    raise

    def changeResults():
        raise NotImplementedError

    def changeDate():
        raise NotImplementedError

    def updatePlayers(self, playerupdate=list):
        self.ioapi.Update(PLAYERS, playerupdate=list)

    def updateTeams(self, teamsupdate=list):
        self.ioapi.Update(PLAYERS, teamsupdate=list)

    def updateGames(self, gamesupdate=list):
        self.ioapi.Update(GAMES, gamesupdate=list)

    def updateTournament(self, tournamentupdate=list):
        self.ioapi.Update(TOURNAMENTS, tournamentupdate=list)

    def updateResults(self, newresults=list, resultsID=str):
        self.ioapi.updateResults(newresults=list, resultsID=str)

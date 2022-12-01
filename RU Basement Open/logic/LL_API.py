from IO.IO_API import IO_API 
from models.player import Player
from models.team import Team
from models.tournament import Tournament
from models.game import Game
from logic.PlayersLL import PlayersLL
from logic.ResultsLL import ResultsLL
from logic.TeamsLL import TeamsLL
from logic.TournamentLL import TournamentLL
from logic.GamesLL import GamesLL

class LL_API:

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi
        self.playersLL = PlayersLL(ioapi)
        self.tournamentsLL = TournamentLL(ioapi)
        self.teamsLL = TeamsLL(ioapi)
        self.resultsLL = ResultsLL(ioapi)
        self.gamesLL = GamesLL(ioapi)

    def getPlayers(self):
        return self.playersLL.getAllPlayers()

    def getTeams(self):
        return self.teamsLL.getAllTeams()

    def getGames(self):
        return self.gamesLL.getAllGames()

    def getTournaments(self):
        return self.tournamentsLL.getAllTournaments()

    def getResults(self, resultsID):
        raise NotImplementedError

    def getPlayerScore(self, playername: str):
        return self.playersLL.getPlayerScore(playername)
         
    def getPlayerScoreByDate(self):
        raise NotImplementedError

    def getTournamentScores(self):
        return self.tournamentsLL.getTournamentScore()

    def getTournamentDates(self):
        return self.tournamentsLL.getTournamentDates()

    def getGamesFinished(self) -> list[Game]:
        return [game for game in self.gamesLL.getAllGames() if game.results is not None]

    def getUpcomingGames(self) -> list[Game]:
        return [game for game in self.gamesLL.getAllGames() if game.results is None]

    def getPlayerList(self) -> list[Player]:
        return self.playersLL.getPlayerList()

    def addPlayer(self, player: Player):
        self.playersLL.addPlayer(player)

    def addTeam(self, team: Team):
        self.teamsLL.addTeam(team)

    def addTournament(self, tournament: Tournament):
        self.tournamentsLL.addTournament(tournament)

    def addGame(self, game: Game):
        self.gamesLL.addGame(game)

    def changeResults():
        raise NotImplementedError

    def changeDate():
        raise NotImplementedError


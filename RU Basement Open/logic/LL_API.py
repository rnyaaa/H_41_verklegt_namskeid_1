from IO.IO_API import IO_API
from models.player import Player
from models.team import Team
from models.teamscore import TeamScore
from models.tournament import Tournament
from models.game import Game
from models.playerscore import PlayerScore
from models.playersummary import PlayerSummary
from logic.PlayersLL import PlayersLL
from logic.ResultsLL import ResultsLL
from logic.TeamsLL import TeamsLL
from logic.TournamentLL import TournamentLL
from logic.GamesLL import GamesLL


class LL_API:

    def __init__(self, ioapi: IO_API):
        """ Gets the io stream and sends to the LL classes """
        self.ioapi = ioapi
        self.playersLL = PlayersLL(ioapi)
        self.tournamentsLL = TournamentLL(ioapi)
        self.teamsLL = TeamsLL(ioapi)
        self.resultsLL = ResultsLL(ioapi)
        self.gamesLL = GamesLL(ioapi)

    def getPlayers(self) -> list[Player]:
        """ returns a list of all Player instances """
        return self.playersLL.getAllPlayers()

    def getTeams(self) -> list[Team]:
        """ returns a list of all Team instances """
        return self.teamsLL.getAllTeams()

    def getTeamScore(self) -> list[TeamScore]:
        """ returns a list of all TeamScore instances"""
        return self.teamsLL.getTeamScore()

    def getTeamScoreSummaries(self, tournamentid) -> list[TeamScore]:
        """ returns a list of all TeamScores summaries for a Tournament"""
        return self.teamsLL.getTeamScoreSummariesByTournament(tournamentid)

    def getTeamNameFromId(self, team_id) -> str:
        """ returns a team name from a team_id """
        return self.teamsLL.getTeamNameFromId(team_id)

    def getGames(self) -> list[Game]:
        """ returns a list of all Games instances """
        return self.gamesLL.getAllGames()


    def getTournaments(self) -> list[Tournament]:
        """ returns a list of all Tournament instances """
        return self.tournamentsLL.getAllTournaments()

    def getResults(self):
        return self.resultsLL.getAllResults()

    def getPlayerScores(self) -> list[PlayerSummary]:
        """ returns a list of Player.name and a list of PlayerScore instances """
        return self.playersLL.getAllPlayerScore()

    def getPlayerScoreSummaries(self) -> list[PlayerSummary]:
        """ returns a list of Player.name and a list of PlayerScore instances """
        return self.playersLL.getPlayerScoreSummaries()

    def getPlayerScoreSummariesByTournament(self, tournamentid) -> list[PlayerSummary]:
        """ returns a list of Player.name and a list of PlayerScore instances """
        return self.playersLL.getPlayerScoreSummariesByTournament(tournamentid)

    def getSinglePlayerScore(self, playerid) -> PlayerSummary:
        """ returns a playersummary for a single player """
        return self.playersLL.getSinglePlayerScore(playerid)

    def getPlayerScoreByDate(self):
        raise NotImplementedError

    def getPlayerNameFromId(self, playerid):
        return self.playersLL.getPlayerNameFromId(playerid)

    def getTournamentScores(self) -> list[tuple[str, int, int]]:
        """ returns a list of tuples containing the team name, games won and rounds won """
        return self.tournamentsLL.getTournamentScore()

    def getTournamentDates(self, tournament_id: str) -> list[Game]:
        """ returns a list of Game instances where the tournament id matches the game.tournament_id """
        return [game for game in self.gamesLL.getAllGames() if game.tournament_id == tournament_id]

    def getGamesFinished(self) -> list[Game]:
        """ returns a list of games where the results are not None(have been filled in, thus are finished) """
        return [game for game in self.gamesLL.getAllGames() if (game.results_awayteam and game.results_hometeam) is not None]

    def getUpcomingGames(self) -> list[Game]:
        """ returns a list of games where the results are None(have not been filled in, thus are upcoming) """
        return [game for game in self.gamesLL.getAllGames() if (game.results_awayteam and game.results_hometeam) is None]

    def getPlayerList(self) -> list[tuple[Player, str]]:
        """ returns a list of tuples of players and the score they are sorted by """
        return self.playersLL.getPlayerList()

    def addPlayer(self, player: Player):
        """ add a player """
        self.playersLL.addPlayer(player)

    def addTeam(self, team: Team):
        """ add a team """
        self.teamsLL.addTeam(team)

    def addTournament(self, tournament: Tournament):
        """ add a tournament """
        self.tournamentsLL.addTournament(tournament)

    def addGame(self, game: Game):
        """ add a game """
        self.gamesLL.addGame(game)

    def changeResults():
        raise NotImplementedError

    def changeDate(self, updated_info):
        self.tournamentsLL.changeTournamentInfo()
    
    def getTournamentNameFromId(self, tournamentid) -> str:
        return self.tournamentsLL.getTournamentNameFromId(tournamentid)

    def verifyTournament(self, new_name):
        data = self.getTournaments()
        for list in data:
            if list.name == new_name:
                print("Nafnið er frátekið, reyndu aftur.")
                return True
            else:
                return False

    def checkIfPlayerIsRegistered(self, player):
        input_player = input(player)
        data = self.getPlayers()
        for list in data:
            if list.name.lower() == input_player.lower():
                return input_player
            else:
                print("Leikmaður er ekki skráður.")

    def getTeam_id(self, team_name):
        """Gets and returns a team ID for a given team name."""
        team_id = self.getTeams()
        for list in team_id:
            if list.name == team_name:
                return list.id

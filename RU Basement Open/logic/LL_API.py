from IO.IO_API import IO_API
from models.player import Player
from models.team import Team
from models.tournament import Tournament
from models.game import Game
from models.playerscore import PlayerScore
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

    def getGames(self) -> list[Game]:
        """ returns a list of all Games instances """
        return self.gamesLL.getAllGames()

    def getTournaments(self) -> list[Tournament]:
        """ returns a list of all Tournament instances """
        return self.tournamentsLL.getAllTournaments()

    def getResults(self, results_id: str):
        raise NotImplementedError

    def getPlayerScore(self, player_id: str) -> tuple[str, list[PlayerScore]]:
        """ returns a tuple of Player.name and a list of PlayerScore instances """
        return self.playersLL.getPlayerScore(player_id)

    def getPlayerScoreByDate(self):
        raise NotImplementedError

    def getTournamentScores(self) -> list[tuple[str, int, int]]:
        """ returns a list of tuples containing the team name, games won and rounds won """
        return self.tournamentsLL.getTournamentScore()

    def getTournamentDates(self, tournament_id: str) -> list[Game]:
        """ returns a list of Game instances where the tournament id matches the game.tournament_id """
        return [game for game in self.gamesLL.getAllGames() if game.tournament_id == tournament_id]

    def getGamesFinished(self) -> list[Game]:
        """ returns a list of games where the results are not None(have been filled in, thus are finished) """
        return [game for game in self.gamesLL.getAllGames() if game.results is not None]

    def getUpcomingGames(self) -> list[Game]:
        """ returns a list of games where the results are None(have not been filled in, thus are upcoming) """
        return [game for game in self.gamesLL.getAllGames() if game.results is None]

    def getPlayerList(self, sort) -> list[tuple[Player, str]]:
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

    def changeDate():
        raise NotImplementedError

    def isPhoneNumber(prompt):
        phone_number = input(prompt)
        try:
            int(phone_number)
            if len(phone_number) == 7:
                return phone_number
            else:
                return ValueError
                print("Símanúmer má aðeins innihalda 7 tölustafi.")
        except ValueError:
            print("Símanúmer má ekki innihalda bókstafi.")

    def verifyTournament(self, new_name):
        data = self.getTournaments()
        print(data)
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

    


    
        

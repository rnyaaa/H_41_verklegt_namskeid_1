from IO.IO_API import IO_API
from models.tournament import Tournament
from models.team import Team
from models.game import Game

class TournamentLL():

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def getAllTournaments(self) -> list[Tournament]:
        """ returns a list of all Tournament instances """
        return self.ioapi.return_model(Tournament)

    def addTournament(self, tournament: Tournament):
        """ add a tournament """
        return self.ioapi.create_model(tournament)

    def getTournamentScore(self):
        all_games = self.ioapi.return_model(Game)
        for game in all_games:
            print(game.gameid)
            print(game.tournament_id)
            print(game.date)
            print(game.results)

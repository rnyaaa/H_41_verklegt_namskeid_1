from IO.IO_API import IO_API
from models.game import Game

class GamesLL():

    def __init__(self, ioapi: IO_API):
        """ gets the io stream """
        self.ioapi = ioapi

    def getAllGames(self) -> list[Game]:
        """ gets a list of all Game instances """
        return self.ioapi.return_model(Game)

    def addGame(self, game: Game):
        """ add a Game """
        self.ioapi.create_model(game)

    def changeDate(self):
        raise NotImplementedError
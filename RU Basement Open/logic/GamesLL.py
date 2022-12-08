from IO.IO_API import IO_API
from models.game import Game

class GamesLL():

    def __init__(self, ioapi: IO_API):
        """Gets the io stream."""
        self.ioapi = ioapi

    def getAllGames(self) -> list[Game]:
        """Gets a list of all Game instances."""
        return self.ioapi.return_model(Game)

    def addGame(self, game: Game):
        """Add a Game."""
        self.ioapi.create_model(game)

    def getGameFromId(self, gameid):
        games = self.getAllGames()
        for game in games:
            if game.gameid == gameid:
                return game

    def changeDateGame(self, updated_info):
        self.ioapi.update(updated_info)
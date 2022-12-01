from IO.IO_API import IO_API
from models.player import Player

class PlayersLL:

    def __init__(self, ioapi_connection: IO_API):
        self.ioapi = ioapi_connection

    def getAllPlayers(self):
        players = self.ioapi.getAll("players")
        player_models = []
        for player in players:
            Player(row[0], row[1], row[2], row[3], row[4])
        return player_models

    def getAllPlayerScore(self):
        playerscore = self.ioapi.getAll("PlayerScore")

    def createPlayer(self, player):
        self.ioapi.create_model(player)

    def addPlayers(self, players):

        # players = LL_API.getPlayers()
        # player = []
        players = []
        for player in players:
            self.players.append(player)


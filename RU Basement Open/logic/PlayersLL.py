from IO.IO_API import IO_API
from logic.ResultsLL import ResultsLL
from models.player import Player
# from LL_API import LL_API


class PlayersLL:

    def __init__(self, ioapi_connection: IO_API):
        self.ioapi = ioapi_connection

    def get_all_players(self):
        players = self.ioapi.getAll("players")
        player_models = []
        for lis in players:
            player_models.append(
                Player(lis[0], lis[1], lis[2], lis[3], lis[4]))
        return player_models

    def createPlayer(self, player):
        self.ioapi.create_model(player)

    def addPlayers(self, players):

        # players = LL_API.getPlayers()
        # player = []
        players = []
        for player in players:
            self.players.append(player)

        # LL_API.updatePlayers(players)

from logic.ResultsLL import ResultsLL
from IO.IO_API import IO_API
# from LL_API import LL_API

class PlayersLL:

        players = []
        def addPlayers(self, players):

                # players = LL_API.getPlayers()
                # player = []

                for player in players:
                        self.players.append(player)

                # LL_API.updatePlayers(players)
        
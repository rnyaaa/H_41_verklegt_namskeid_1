from logic.ResultsLL import ResultsLL
from IO.IO_API import IO_API
from LL_API import LL_API



class PlayersLL:

        def addPlayer(playeradd):
                players = LL_API.getPlayers()
                player = []
                for items in playeradd:
                        player.append(items)
                players.append(player)
                LL_API.updatePlayers(players)
        
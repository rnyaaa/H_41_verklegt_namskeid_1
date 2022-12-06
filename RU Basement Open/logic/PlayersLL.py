from IO.IO_API import IO_API
from models.player import Player
from models.playerscore import PlayerScore

class PlayersLL:

    def __init__(self, ioapi: IO_API):
        """ gets the io stream """
        self.ioapi = ioapi

    def getAllPlayers(self) -> list[Player]:
        """ returns a list of all Player instances """
        return self.ioapi.return_model(Player)

    def getAllPlayerScore(self) -> list[PlayerScore]:
        """ returns a list of all PlayerScore instances """
        return self.ioapi.return_model(PlayerScore)

    def addPlayer(self, player: Player):
        """ adds a player """
        self.ioapi.create_model(player)

    def getPlayerScoreSummarized(self) -> list[PlayerScore]:
        playerscores = self.getAllPlayerScore
        players = []
        for item in playerscores:
            if item[0] not in players:
                players.append(item[0])
            if item[0] in players:
                players[item][1] = players[item]


    def getPlayerScoreByDate():
        raise NotImplementedError
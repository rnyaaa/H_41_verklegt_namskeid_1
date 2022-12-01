from IO.IO_API import IO_API
from models.player import Player
from models.playerscore import PlayerScore

class PlayersLL:

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def getAllPlayers(ioapi):
        players = ioapi.getAll(Player)
        player_models = []
        for player in players:
            player_models.append(Player(player[0], player[1], player[2], player[3], player[4]))
        return player_models

    def getAllPlayerScore(self):
        scores = self.ioapi.return_model(PlayerScore)

    def createPlayer(self, player):
        self.ioapi.create_model(player)

    def getPlayerScores(self):
        playerscores = self.ioapi.getAll(PlayerScore)
        scores = []
        for score in playerscores:
            scores.append(PlayerScore(score[0], score[1], score[2], score[3], score[3]))
        return scores
            

    def getPlayerList(self, sortkey):
        players = self.ioapi.getAll(Player)
        playerlist = []
        for player in players:
            playerlist.append(player.name)

    def getPlayerScore(self, name):
        """ Takes the playerstream, finds the player and takes the values from 8-19 and puts them in an array and returns it """
        players = self.ioapi.getPlayers()
        scores = []
        player = None
        for p in players:
            if p.name == name:
                player = p
            # if players[player][0] == playername:
            #     scores = [line[8], line[9], line[10], line[11], line[12], line[13],
            #               line[14], line[15], line[16], line[17], line[18], line[19]]
            #     """ 501 Einmenn, unnir, tap, 301 Duo, unnir, tap, Cricket, unnir, tap,501 Fjormenn, unnir, tap"""
        return scores

    def getPlayerScoreByDate():
        raise NotImplementedError
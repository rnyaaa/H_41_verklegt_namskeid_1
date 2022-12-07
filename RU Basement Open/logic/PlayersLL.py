from IO.IO_API import IO_API
from models.player import Player
from models.playerscore import PlayerScore
from models.playersummary import PlayerSummary

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

    def getPlayerScoresSummarized(self) -> list[PlayerSummary]:
        playerscores = self.getAllPlayerScore()
        """ get all PlayerScores in dict with the playerid as a key for each of their respective playerscores """
        playerscores_by_player = dict()
        for item in playerscores:
            if item.playerid in playerscores_by_player:
                playerscores_by_player[item.playerid].append(item)
            else:
                playerscores_by_player[item.playerid] = [item]
        
        player_summaries = []
        for player_id in playerscores_by_player:
            """ get PlayerSummary with default values """
            player_summary = PlayerSummary(player_id)
            for score in playerscores_by_player[player_id]:
                player_summary.QPs += score.QPs
                player_summary.inshots = max(player_summary.inshots, score.inshots)
                player_summary.outshots = max(player_summary.outshots, score.outshots)
                player_summary.result501singles[0] += score.result501singles[0]
                player_summary.result501singles[1] += score.result501singles[1]
                player_summary.result301[0] += score.result301[0]
                player_summary.result301[1] += score.result301[1]
                player_summary.resultcricket[0] += score.resultcricket[0]
                player_summary.resultcricket[1] += score.resultcricket[1]
                player_summary.result501fours[0] += score.result501fours[0]
                player_summary.result501fours[1] += score.result501fours[1]
            player_summaries.append(player_summary)
        return player_summaries

    def getPlayerScoresSummarizedbyTournament(self, tournamentid) -> list[PlayerSummary]:
        playerscores = self.getAllPlayerScore()
        """ get all PlayerScores in dict with the playerid as a key for each of their respective playerscores """
        playerscores_by_player = dict()
        for item in playerscores:
            if item.playerid in playerscores_by_player and item.tournamentid == tournamentid:
                playerscores_by_player[item.playerid].append(item)
            else:
                playerscores_by_player[item.playerid] = [item]
        
        player_summaries = []
        for player_id in playerscores_by_player:
            """ get PlayerSummary with default values """
            player_summary = PlayerSummary(player_id)
            for score in playerscores_by_player[player_id]:
                player_summary.QPs += score.QPs
                player_summary.inshots = max(player_summary.inshots, score.inshots)
                player_summary.outshots = max(player_summary.outshots, score.outshots)
                player_summary.result501singles[0] += score.result501singles[0]
                player_summary.result501singles[1] += score.result501singles[1]
                player_summary.result301[0] += score.result301[0]
                player_summary.result301[1] += score.result301[1]
                player_summary.resultcricket[0] += score.resultcricket[0]
                player_summary.resultcricket[1] += score.resultcricket[1]
                player_summary.result501fours[0] += score.result501fours[0]
                player_summary.result501fours[1] += score.result501fours[1]
            player_summaries.append(player_summary)
        return player_summaries


    def getSinglePlayerScore(self, playerid) -> PlayerSummary:
        """ gets the PlayerSummary of a single player by playerid """
        player_summaries = self.getPlayerScoresSummarized()
        for player_summary in player_summaries:
            if player_summary.playerid == playerid:
                return player_summary

    def getPlayersSorted(self, sortBy):
        """ get player list sorted by one of the functions below. You need to replace "sortBy" with one of the functions below """
        """ e.g. calling this function as getPlayersSorted(ByQualityPoints())"""
        return sorted(self.getPlayerScoresSummarized(), key=sortBy)

    def getPlayerNameFromId(self, playerid):
        players = self.getAllPlayers()
        for item in players:
            if item.playerid == playerid:
                return item.name

    def ByQualityPoints(player_summary: PlayerSummary):
        return player_summary.QPs

    def ByInshots(player_summary: PlayerSummary):
        return player_summary.inshots

    def ByOutshots(player_summary: PlayerSummary):
        return player_summary.outshots

    def getPlayerScoreByDate():
        raise NotImplementedError
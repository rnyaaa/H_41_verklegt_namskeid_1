from IO.IO_API import IO_API
from models.game import Game
from models.player import Player
from models.playerscore import PlayerScore
from models.playersummary import PlayerSummary
import datetime

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

    def addPlayerScore(self, playerscore: PlayerScore):
        """ add a playerscore"""
        self.ioapi.create_model(playerscore)

    def getPlayerScoreSummaries(self) -> list[PlayerSummary]:
        playerscores = self.getAllPlayerScore()
        """ get all PlayerScores in dict with the playerid as a key for each of their respective playerscores """
        playerscores_by_player = {}
        # rennir í gegnum PlayerScores og safnar þeim í dict lyklað með playerid, þannig playerids geyma öll playerscorein
        for item in playerscores:
            if item.playerid in playerscores_by_player:
                playerscores_by_player[item.playerid].append(item)
            else:
                playerscores_by_player[item.playerid] = [item]
        
        player_summaries = []
        # síðan loopar það í gegnum dictið og býr til PlayerSummary fyrir hvern player úr niðurstöðunum sem leikmaður er skráður með í dictinu
        for player_id in playerscores_by_player:
            """ get PlayerSummary with default values """
            player_summary = PlayerSummary(player_id, 0, 0, 0 , [0, 0], [0, 0], [0, 0], [0, 0])
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

    def getPlayerScoreSummariesByTournament(self, tournamentid) -> list[PlayerSummary]:
        # þetta sækir playerscores nema filterar út öll playerscores úr öðru tournament
        playerscores = [score for score in self.getAllPlayerScore() if score.tournamentid == tournamentid]
        """ get all PlayerScores in dict with the playerid as a key for each of their respective playerscores """
        playerscores_by_player = {}
        for item in playerscores:
            if item.playerid in playerscores_by_player:
                playerscores_by_player[item.playerid].append(item)
            else:
                playerscores_by_player[item.playerid] = [item]
        
        # gerir síðan það sama með þau playerscores og í getPlayerScoreSummaries: loopar í gegnum dictið og býr til PlayerSummary fyrir hvern player úr niðurstöðunum
        player_summaries = []
        for player_id in playerscores_by_player:
            """ get PlayerSummary with default values """
            player_summary = PlayerSummary(player_id, 0, 0, 0 , [0, 0], [0, 0], [0, 0], [0, 0])
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
        player_summaries = self.getPlayerScoreSummaries()
        for player_summary in player_summaries:
            if player_summary.playerid == playerid:
                return player_summary
        

    def getPlayersSorted(self, sortBy):
        """ get player list sorted by one of the functions below. You need to replace "sortBy" with one of the functions below """
        """ e.g. calling this function as getPlayersSorted(ByQualityPoints())"""
        return sorted(self.getPlayerScoreSummaries(), key=sortBy)

    def getPlayerNameFromId(self, playerid):
        """returns a player name for """
        players = self.getAllPlayers()
        for item in players:
            if item.playerid == playerid:
                return item.name

    def getPlayerScoreByDate(self, playerid, date):
        """ returns a playersummary for a player from a given date"""
        allplayerscores = self.getAllPlayerScore()
        playerscorebydate = []
        # finnur öll playerscores fyrir leikmanninn
        for score in allplayerscores:
            if score.playerid == playerid:
                # fær dagsetningu leikja með því að fá alla leiki
                all_games = self.ioapi.return_model(Game)
                # passar að leikmaður sé í þeim leikjum
                for indexed_game in all_games:
                    if indexed_game.id == score.id:
                        game = indexed_game
                # filterar út síðan playerscores sem gerðust fyrir gefna dagsetningu
                if datetime.datetime.strptime(game.date, '%d.%m.%y') >= datetime.datetime.strptime(date, '%d.%m.%y'):
                    playerscorebydate.append(score)
        # býr til PlayerSummary úr þeim playerscore föllum
        PlayerSummaryByDate = PlayerSummary(playerid, 0, 0, 0 , [0, 0], [0, 0], [0, 0], [0, 0])
        for score in playerscorebydate:
                PlayerSummaryByDate.QPs += score.QPs
                PlayerSummaryByDate.inshots = max(PlayerSummaryByDate.inshots, score.inshots)
                PlayerSummaryByDate.outshots = max(PlayerSummaryByDate.outshots, score.outshots)
                PlayerSummaryByDate.result501singles[0] += score.result501singles[0]
                PlayerSummaryByDate.result501singles[1] += score.result501singles[1]
                PlayerSummaryByDate.result301[0] += score.result301[0]
                PlayerSummaryByDate.result301[1] += score.result301[1]
                PlayerSummaryByDate.resultcricket[0] += score.resultcricket[0]
                PlayerSummaryByDate.resultcricket[1] += score.resultcricket[1]
                PlayerSummaryByDate.result501fours[0] += score.result501fours[0]
                PlayerSummaryByDate.result501fours[1] += score.result501fours[1]
        return PlayerSummaryByDate


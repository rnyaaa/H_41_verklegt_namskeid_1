from IO.IO_API import IO_API
from models.results import Results
from models.player import Player
from models.team import Team
from models.game import Game
from models.teamscore import TeamScore
from models.playerscore import PlayerScore

class ResultsLL:

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def changeResults(self, teams, playerscores, resultlist, game, gameslist):
        games_to_update = self.getAllGames()
        playerscores_to_update = self.getAllPlayerScore()
        teamscores_to_update = self.getTeamScore()
        for update in games_to_update:
            if update.id == game.id:
                update.results_hometeam = None
                update.results_awayteam = None
        self.ioapi.overwrite_model(games_to_update)
        for item in playerscores_to_update:
            for playerscore in playerscores:
                if item.id == playerscore.id:
                    playerscore.tournamentid = 0
                    playerscore.playerid = 0
                    playerscore.QPs = 0
                    playerscore.inshots = 0
                    playerscore.outshots = 0
                    playerscore.result501singles = 0
                    playerscore.result301 = 0
                    playerscore.resultcricket = 0
                    playerscore.result501fours = 0
        self.ioapi.overwrite_model(playerscores_to_update)
        for item in teamscores_to_update:
            if item.game_id == game.id:
                item.tournament_id = 0
                item.games_won = 0
                item.rounds_won = 0
        self.ioapi.overwrite_model(teamscores_to_update)
        self.addResults(teams, playerscores, resultlist, game, gameslist)
        



    def getTeamScore(self) -> list[TeamScore]:
        """ returns a list of all TeamScore instances """
        return self.ioapi.return_model(TeamScore)
    
    def getAllPlayerScore(self) -> list[PlayerScore]:
        """ returns a list of all PlayerScore instances """
        return self.ioapi.return_model(PlayerScore)

    def getAllGames(self) -> list[Game]:
        """Gets a list of all Game instances."""
        return self.ioapi.return_model(Game)
    
    def addResults(self, teams, playerscores, resultlist, game, gameslist):
        """ adds results """
        game_score_home = 0
        game_away_score = 0
        home_score_rounds = 0
        away_score_rounds = 0
        for result in resultlist:
            home_score_rounds += result.home_score 
            away_score_rounds += result.away_score
            for playerscore in playerscores:
                for players in result.home_players:
                    if result.game_type == "501 1v1":
                        if players.playerid == playerscore.playerid:
                            if result.home_score > result.away_score:
                                playerscore.result501singles[0] += 1
                            else:
                                playerscore.result501singles[1] += 1
                    if result.game_type == "301 2v2":
                        if players.playerid == playerscore.playerid:
                            if result.home_score > result.away_score:
                                playerscore.result301[0] += 1
                            else:
                                playerscore.result301[1] += 1
                    if result.game_type == "Cricket 2v2":
                        if players.playerid == playerscore.playerid:
                            if result.home_score > result.away_score:
                                playerscore.resultcricket[0] += 1
                            else:
                                playerscore.resultcricket[1] += 1
                    if result.game_type == "501 4v4":
                        if players.playerid == playerscore.playerid:
                            if result.home_score > result.away_score:
                                playerscore.result501fours[0] += 1
                            else:
                                playerscore.result501fours[1] += 1
                for players in result.away_players:
                    if result.game_type == "501 1v1":
                        if players.playerid == playerscore.playerid:
                            if result.away_score > result.home_score:
                                playerscore.result501singles[0] += 1
                            else:
                                playerscore.result501singles[1] += 1
                    if result.game_type == "301 2v2":
                        if players.playerid == playerscore.playerid:
                            if result.away_score > result.home_score:
                                playerscore.result301[0] += 1
                            else:
                                playerscore.result301[1] += 1
                    if result.game_type == "Cricket 2v2":
                        if players.playerid == playerscore.playerid:
                            if result.away_score > result.home_score:
                                playerscore.resultcricket[0] += 1
                            else:
                                playerscore.resultcricket[1] += 1
                    if result.game_type == "501 4v4":
                        if players.playerid == playerscore.playerid:
                            if result.away_score > result.home_score:
                                playerscore.result501fours[0] += 1
                            else:
                                playerscore.result501fours[1] += 1

        for result in resultlist:
            if result.home_score > result.away_score:
                game_score_home += 1
            else:
                game_away_score += 1
        
        teams[0].rounds_won = home_score_rounds
        teams[0].games_won = game_score_home
        teams[1].rounds_won = away_score_rounds
        teams[1].games_won = game_away_score
        for playerscore in playerscores:
            self.ioapi.create_model(playerscore)

        self.ioapi.create_model(teams[0])
        self.ioapi.create_model(teams[1])

        for indexed_game in gameslist:
            if indexed_game.id == game.id:
                indexed_game.results_hometeam = game_score_home
                indexed_game.results_awayteam = game_away_score
                self.ioapi.update(indexed_game)
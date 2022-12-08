from dataclasses import dataclass

from models.player import Player
from logic.LL_API import LL_API
from models.playerscore import PlayerScore
from models.teamscore import TeamScore
from models.tournament import Tournament
from models.player import Player
from ui.UI import Menu_functions
from ui.OrganizerUI import OrganizerUI


@dataclass
class GameResult:
    game_type: str
    home_players: list[Player]
    away_players: list[Player]

    home_score: int
    away_score: int


class CaptainUI():

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayCaptainUI(self):
        while True:
            print(78*"_")
            print(
                "\nVelkominn, Fyrirliði.\n"
                "\n\n"
                "➢  Valmynd:\n"
                "\n"
                "1.  Skrá úrslit viðureignar")
            user_input = Menu_functions.menuFooter(True)

            if user_input == "1":
                self.addResults()
            elif user_input == "b":
                break
            elif user_input == "q":
                Menu_functions.menuQuit()
            else:
                print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.")

    def addResults(self):
        tournament = OrganizerUI.select_tournament_input(self)
        game = self.select_game_input(tournament.name, tournament.id)

        home_team_id = self.llapi.getTeam_id(game.home_team)
        away_team_id = self.llapi.getTeam_id(game.away_team)

        home_players = self.llapi.getPlayersFromTeam(home_team_id)
        away_players = self.llapi.getPlayersFromTeam(away_team_id)

        if len(home_players) < 4:
            print(
                f"\n⛔ Of fáir leikmenn í {game.home_team} (heimaliðið). Lið verður að hafa að lágmarki 4 leikmenn.")
            return
        if len(away_players) < 4:
            print(
                f"\n⛔ Of fáir leikmenn í {game.away_team} (útiliðið). Lið verður að hafa að lágmarki 4 leikmenn.")
            return

        resultlist = []
        # allar 501 1v1 umferðirnar, niðurstöður:
        print("\n****************************")
        print(" Skráning á leik 501 - 1v1:")
        print("****************************")
        result_501_1v1_1 = self.get_501_1v1_results(home_team_id, away_team_id)
        result_501_1v1_2 = self.get_501_1v1_results(home_team_id, away_team_id)
        result_501_1v1_3 = self.get_501_1v1_results(home_team_id, away_team_id)
        result_501_1v1_4 = self.get_501_1v1_results(home_team_id, away_team_id)
        resultlist.append(result_501_1v1_1, result_501_1v1_2, result_501_1v1_3, result_501_1v1_4)

        # niðurstaða 301 umferðarinnar:
        print("\n****************************")
        print(" Skráning á leik 301 - 2v2:")
        print("****************************")
        result_301_2v2 = self.get_301_results(home_team_id, away_team_id)
        resultlist.append(result_301_2v2)

        # niðurstaða cricket:
        print("\n****************************")
        print(" Skráning á leik C - 2v2:\n")
        print("****************************")
        result_cricket = self.get_cricket_results(home_team_id, away_team_id)
        resultlist.append(result_cricket)

        # niðurstaða 501 4v4 umferðarinnar:
        print("\n****************************")
        print(" Skráning á leik 501 - 4v4:")
        print("****************************")
        result_501_4v4 = self.get_501_4v4_results(home_team_id, away_team_id)
        resultlist.append(result_501_4v4)

        playerscores = []
        for player in home_players:
            playerscores.append(PlayerScore(tournament.id, game.gameid, player.playerid))
        for player in away_players:
            playerscores.append(PlayerScore(tournament.id, game.gameid, player.playerid))

        # Stigagjöf - QPs, Innskot og Útskot
        print("\n****************************")
        print(" Skráning á Stigum: ")
        print("****************************")
        playerscores = self.get_PlayerScores(playerscores)

        home_team_score = TeamScore(home_team_id, tournament.id, game.gameid)
        away_team_score = TeamScore(away_team_id, tournament.id, game.gameid)
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
        
        home_team_score.rounds_won = home_score_rounds
        home_team_score.games_won = game_score_home
        away_team_score.rounds_won = away_score_rounds
        away_team_score.games_won = game_away_score
        for playerscore in playerscores:
            self.llapi.addPlayerScore(playerscore)

        self.llapi.addTeamScore(home_team_score)
        self.llapi.addTeamScore(away_team_score)

        gameslist = self.llapi.getUpcomingGames()
        for indexed_game in gameslist:
            if indexed_game.gameid == game.gameid:
                indexed_game.results_hometeam = game_score_home
                indexed_game.results_awayteam = game_away_score
        self.llapi.updateGame(indexed_game)

        # --------------------------------------- LAGA HÉÐAN (ER BÚINN AÐ GERA FYRIR OFAN ÞETTA) ------------------------------------------------

        #PlayerScore(tournament.id, game.id, playerid, qps, inshot, outshot,
                    #result501singles_wins, result301_wins, resultcricket_wins, result501fours_wins)

        #TeamScore()


# hér f neðan eru öll föllin sem captain UI samanstendur af tíhí


    def get_501_1v1_results(self, home_team_id, away_team_id):
        home_player = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id)
        away_player = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id)

        home_score = 0
        away_score = 0

        while home_score < 2 and away_score < 2:
            new_home_score, new_away_score = self.who_won(home_player.name,away_player.name)
            home_score += new_home_score
            away_score += new_away_score

        return GameResult("501 1v1", [home_player], [away_player], home_score, away_score)

    def get_301_results(self, home_team_id, away_team_id):
        home_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id)
        home_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid])
        away_player1 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id)
        away_player2 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, [away_player1.playerid])

        home_score = 0
        away_score = 0

        while home_score < 2 and away_score < 2:
            new_home_score, new_away_score = self.who_won()
            home_score += new_home_score
            away_score += new_away_score

        return GameResult("301 2v2", [home_player1, home_player2], [away_player1, away_player2], home_score, away_score)

    def get_cricket_results(self, home_team_id, away_team_id):
        home_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id)
        home_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid])
        away_player1 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id)
        away_player2 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, [away_player1.playerid])

        home_score = 0
        away_score = 0

        while home_score < 2 and away_score < 2:
            new_home_score, new_away_score = self.who_won()
            home_score += new_home_score
            away_score += new_away_score

        return GameResult("Cricket 2v2", [home_player1, home_player2], [away_player1, away_player2], home_score, away_score)

    def get_501_4v4_results(self, home_team_id, away_team_id):
        home_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id)
        home_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid])
        home_player3 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid, home_player2.playerid])
        home_player4 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid, home_player2.playerid, home_player3.playerid])
        away_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", away_team_id)
        away_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", away_team_id, [away_player1.playerid])
        away_player3 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", away_team_id, [away_player1.playerid, away_player2.playerid])
        away_player4 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", away_team_id, [away_player1.playerid, away_player2.playerid, away_player3.playerid])

        home_score = 0
        away_score = 0

        while home_score < 2 and away_score < 2:
            new_home_score, new_away_score = self.who_won()
            home_score += new_home_score
            away_score += new_away_score

        return GameResult("501 4v4", [home_player1, home_player2, home_player3, home_player4], [away_player1, away_player2, away_player3, away_player4], home_score, away_score)

    def getPlayerScores(self, playerscores):
        for playerscore in playerscores:
            print(f"Stigagjöf fyrir {self.llapi.getPlayerNameFromId(playerscore.playerid)}")
            playerscore.QPs = input("Hversu mörg Quality Points fékk leikmaðurinn? - 0 ef engin")
            playerscore.inshots = input("Hvað var hæsta innskotið hjá leikmanninum?")
            playerscore.outshots = input("Hvað var hæsta útskot hjá leikmanninum?")
        return playerscore



    def select_game_input(self, tournament_name, tournament_id):
        """Prints a numbered list of all games and asks the user for their selection. The selected game index is returned"""

        print(f"\n{tournament_name} - yfirlit\n\nVeljið viðureign:\n")
        upcoming_games = self.llapi.getUpcomingGames()
        upcoming_games_in_tournament = [
            game for game in upcoming_games if game.tournament_id == tournament_id]
        command = ""
        while True:
            for i, game in enumerate(upcoming_games_in_tournament):
                print(f"{i+1}. {game.home_team} vs. {game.away_team}")
            try:
                command = int(
                    input(f"\nVeldu viðureign af listanum hér fyrir ofan (sláðu inn tölustafinn á viðureigninni sem þú vilt velja): "))
                if command < 1 or command > len(upcoming_games):
                    print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")
                    continue
                break
            except ValueError:
                print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")
        return upcoming_games[command-1]

    def select_teamplayer_input(self, ui_str, team_id, exclude_ids=[]):
        """Prints a numbered list of all players of a team and asks the user for their selection. The selected player's id is returned"""
        print(ui_str)
        players = self.llapi.getPlayers()

        filtered_players = [
            player for player in players if player.team_id == team_id and player.playerid not in exclude_ids]
        command = ""
        while True:
            for i in range(len(filtered_players)):
                print(i+1, ". ", filtered_players[i].name)
            try:
                command = int(
                    input(f"\nVeldu leikmann af listanum hér fyrir ofan (sláðu inn númer þess leikmanns sem þú vilt velja): "))
                if command < 1 or command > len(filtered_players):
                    print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")
                    continue
                return filtered_players[command-1]
            except:
                print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")

    def who_won(self, home_player, away_player):
        print("Hver vann 1. umferð?\n")
        print(f"a. {home_player}")
        print(f"b. {away_player}")
        #print("a. heimalið")
        #print("b. útilið\n")

        while True:
            user_input = input(
                "Sláðu inn valmöguleika af listanum hér að ofan: ")
            if user_input == "a":
                return (1, 0)
            if user_input == "b":
                return (0, 1)
            print('⛔ Ekki gildur valmöguleiki, reyndu aftur')

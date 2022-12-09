from dataclasses import dataclass

from models.player import Player
from logic.LL_API import LL_API
from models.playerscore import PlayerScore
from models.teamscore import TeamScore
from models.tournament import Tournament
from models.player import Player
from ui.UI import Menu_functions
from ui.OrganizerUI import OrganizerUI
import os


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

    def scoring_Header_Print(self, type):
        """Prints the results registration header for appropriate game types."""
        if type == "501s":
            print("\n****************************")
            print(" Skráning á leik 501 - 1v1:")
            print("****************************")
        if type == "301":
            print("\n****************************")
            print(" Skráning á leik 301 - 2v2:")
            print("****************************")
        if type == "C":
            print("\n****************************")
            print(" Skráning á leik C - 2v2:")
            print("****************************")
        if type == "501f":
            print("\n****************************")
            print(" Skráning á leik 501 - 4v4:")
            print("****************************")
        if type == "score":
            print("\n****************************")
            print(" Skráning á Stigum: ")
            print("****************************\n")

    def addResults(self):
        "Results registration process for team captain."
        os.system('cls||clear')
        tournament = OrganizerUI.select_tournament_input(self)
        os.system('cls||clear')
        game = self.select_game_input(tournament.id)

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
        exclude = []
        # allar 501 1v1 umferðirnar, niðurstöður:
        result_501_1v1_1 = self.get_501_1v1_results(
            home_team_id, away_team_id, [])
        for player in result_501_1v1_1.home_players:
            exclude.append(player.playerid)
        for player in result_501_1v1_1.away_players:
            exclude.append(player.playerid)
        result_501_1v1_2 = self.get_501_1v1_results(
            home_team_id, away_team_id, exclude)
        for player in result_501_1v1_2.home_players:
            exclude.append(player.playerid)
        for player in result_501_1v1_2.away_players:
            exclude.append(player.playerid)
        result_501_1v1_3 = self.get_501_1v1_results(
            home_team_id, away_team_id, exclude)
        for player in result_501_1v1_3.home_players:
            exclude.append(player.playerid)
        for player in result_501_1v1_3.away_players:
            exclude.append(player.playerid)
        result_501_1v1_4 = self.get_501_1v1_results(
            home_team_id, away_team_id, exclude)
        resultlist.append(result_501_1v1_1)
        resultlist.append(result_501_1v1_2)
        resultlist.append(result_501_1v1_3)
        resultlist.append(result_501_1v1_4)

        # niðurstaða 301 umferðarinnar:
        result_301_2v2 = self.get_301_results(home_team_id, away_team_id)
        resultlist.append(result_301_2v2)

        # niðurstaða cricket:
        exclude = []
        for player in result_301_2v2.home_players:
            exclude.append(player.playerid)
        for player in result_301_2v2.away_players:
            exclude.append(player.playerid)
        result_cricket = self.get_cricket_results(
            home_team_id, away_team_id, exclude)
        resultlist.append(result_cricket)

        # niðurstaða 501 4v4 umferðarinnar:
        result_501_4v4 = self.get_501_4v4_results(home_team_id, away_team_id)
        resultlist.append(result_501_4v4)

        playerscores = []
        for player in home_players:
            playerscores.append(PlayerScore(
                player.playerid, game.id, tournament.id))
        for player in away_players:
            playerscores.append(PlayerScore(
                player.playerid, game.id, tournament.id))

        # Stigagjöf - QPs, Innskot og Útskot
        playerscores = self.getPlayerScores(playerscores)

        teams = [TeamScore(home_team_id, tournament.id, game.id), TeamScore(
            away_team_id, tournament.id, game.id)]
        gameslist = self.llapi.getUpcomingGames()
        self.llapi.addResults(teams, playerscores, resultlist, game, gameslist)

        os.system('cls||clear')
        print("✅ Niðurstöður skráðar!")
        Menu_functions.pressEnterToContinue()

    def get_501_1v1_results(self, home_team_id, away_team_id, exclude_ids):
        """"Gets and returns results from a 1v1 player 510 game."""
        os.system('cls||clear')
        self.scoring_Header_Print("501s")
        home_player = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, exclude_ids)
        os.system('cls||clear')
        self.scoring_Header_Print("501s")
        away_player = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, exclude_ids)

        home_score = 0
        away_score = 0
        counter = 1
        while home_score < 2 and away_score < 2:
            os.system('cls||clear')
            self.scoring_Header_Print("501s")
            new_home_score, new_away_score = self.who_won(
                home_player.name, away_player.name, counter)
            home_score += new_home_score
            away_score += new_away_score
            counter += 1

        return GameResult("501 1v1", [home_player], [away_player], home_score, away_score)

    def get_301_results(self, home_team_id, away_team_id):
        """"Gets and returns results from a 2v2 player 310 game."""
        os.system('cls||clear')
        self.scoring_Header_Print("301")
        home_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id)
        os.system('cls||clear')
        self.scoring_Header_Print("301")
        home_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid])
        os.system('cls||clear')
        self.scoring_Header_Print("301")
        away_player1 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id)
        os.system('cls||clear')
        self.scoring_Header_Print("301")
        away_player2 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, [away_player1.playerid])
        os.system('cls||clear')

        home_score = 0
        away_score = 0
        counter = 1
        while home_score < 2 and away_score < 2:
            os.system('cls||clear')
            self.scoring_Header_Print("301")
            new_home_score, new_away_score = self.who_won(self.llapi.getTeamNameFromId(
                home_team_id), self.llapi.getTeamNameFromId(away_team_id), counter)
            home_score += new_home_score
            away_score += new_away_score
            counter += 1

        return GameResult("301 2v2", [home_player1, home_player2], [away_player1, away_player2], home_score, away_score)

    def get_cricket_results(self, home_team_id, away_team_id, exclude_ids):
        """"Gets and returns results from a 2v2 player cricket game."""
        os.system('cls||clear')
        self.scoring_Header_Print("C")
        home_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, exclude_ids)
        os.system('cls||clear')
        self.scoring_Header_Print("C")
        exclude_ids.append(home_player1.playerid)
        home_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, exclude_ids)
        os.system('cls||clear')
        self.scoring_Header_Print("C")
        away_player1 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, exclude_ids)
        os.system('cls||clear')
        self.scoring_Header_Print("C")
        exclude_ids.append(away_player1.playerid)
        away_player2 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, exclude_ids)
        os.system('cls||clear')

        home_score = 0
        away_score = 0
        counter = 1
        while home_score < 2 and away_score < 2:
            os.system('cls||clear')
            self.scoring_Header_Print("301")
            new_home_score, new_away_score = self.who_won(self.llapi.getTeamNameFromId(
                home_team_id), self.llapi.getTeamNameFromId(away_team_id), counter)
            home_score += new_home_score
            away_score += new_away_score
            counter += 1

        return GameResult("Cricket 2v2", [home_player1, home_player2], [away_player1, away_player2], home_score, away_score)

    def get_501_4v4_results(self, home_team_id, away_team_id):
        """"Gets and returns results from a 4v4 player 510 game."""
        os.system('cls||clear')
        self.scoring_Header_Print("501f")
        home_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id)
        os.system('cls||clear')
        self.scoring_Header_Print("501f")
        home_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid])
        os.system('cls||clear')
        self.scoring_Header_Print("501f")
        home_player3 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid, home_player2.playerid])
        os.system('cls||clear')
        self.scoring_Header_Print("501f")
        home_player4 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid, home_player2.playerid, home_player3.playerid])
        os.system('cls||clear')
        self.scoring_Header_Print("501f")
        away_player1 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id)
        os.system('cls||clear')
        self.scoring_Header_Print("501f")
        away_player2 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, [away_player1.playerid])
        os.system('cls||clear')
        self.scoring_Header_Print("501f")
        away_player3 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, [away_player1.playerid, away_player2.playerid])
        os.system('cls||clear')
        self.scoring_Header_Print("501f")
        away_player4 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, [away_player1.playerid, away_player2.playerid, away_player3.playerid])
        os.system('cls||clear')
        self.scoring_Header_Print("501f")

        home_score = 0
        away_score = 0
        counter = 1
        while home_score < 2 and away_score < 2:
            os.system('cls||clear')
            self.scoring_Header_Print("501f")
            new_home_score, new_away_score = self.who_won(self.llapi.getTeamNameFromId(
                home_team_id), self.llapi.getTeamNameFromId(away_team_id), counter)
            home_score += new_home_score
            away_score += new_away_score
            counter += 1

        return GameResult("501 4v4", [home_player1, home_player2, home_player3, home_player4], [away_player1, away_player2, away_player3, away_player4], home_score, away_score)

    def getPlayerScores(self, playerscores):
        """Gets QPs inshots and outshots for a given player."""
        for playerscore in playerscores:
            os.system('cls||clear')
            self.scoring_Header_Print("score")
            print(
                f"Stigagjöf fyrir {self.llapi.getPlayerNameFromId(playerscore.playerid)}: \n")
            playerscore.QPs = input(
                "Hversu mörg Quality Points fékk leikmaðurinn? - 0 ef engin: ")
            playerscore.inshots = input(
                "Hvað var hæsta innskotið hjá leikmanninum?: ")
            playerscore.outshots = input(
                "Hvað var hæsta útskot hjá leikmanninum?: ")
        return playerscores

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

    def who_won(self, home_player, away_player, counter):
        """Ask the user which player won between home player and away player"""

        while True:
            print(f"Hver vann {counter}. umferð?\n")
            print(f"a. {home_player}")
            print(f"b. {away_player}")
            user_input = input(
                f"\nSláðu inn valmöguleika af listanum hér að ofan (t.d. a fyrir {home_player}): ")
            if user_input == "a":
                return (1, 0)
            if user_input == "b":
                return (0, 1)
            print('\n⛔ Ekki gildur valmöguleiki, reyndu aftur\n')

    def select_game_input(self, tournament_id):
        os.system('cls||clear')
        """Prints a numbered list of all games and asks the user for their selection. The selected game index is returned"""

        print(f"\nBreyta Niðurstöðu\n\nVeljið viðureign:\n")
        games_upcoming = self.llapi.getUpcomingGames()
        games_upcoming_in_tournament = [
            game for game in games_upcoming if game.tournament_id == tournament_id]
        while True:
            for i, game in enumerate(games_upcoming_in_tournament):
                print(f"{i+1}. {game.home_team} vs. {game.away_team}")
            try:
                command = int(
                    input(f"\nVeldu viðureign af listanum hér fyrir ofan (sláðu inn tölustafinn á viðureigninni sem þú vilt velja): "))
                if command < 1 or command > len(games_upcoming_in_tournament):
                    print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")
                    continue
                break
            except ValueError:
                print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")

        print("select_game_input check")
        return games_upcoming_in_tournament[command-1]

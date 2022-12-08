from dataclasses import dataclass
from logic.LL_API import LL_API
from models.game import Game
from models.player import Player
from models.playerscore import PlayerScore
from models.teamscore import TeamScore
from models.team import Team
from models.tournament import Tournament
from ui.UI import Menu_functions
import os


@dataclass
class GameResult():
    game_type: str
    home_players: list[Player]
    away_players: list[Player]

    home_score: int
    away_score: int

class OrganizerUI():

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayOrganizerMenu(self):
        os.system('cls||clear')
        """Displays the organizer submenu."""
        while True:
            print(78*"_")
            print()
            print(
                "Velkominn, mótshaldari!\n\n"

                "➢  Valmynd:\n\n"

                "1.	Stofna deild/mót\n"
                "2.	Skrá lið\n"
                "3.	Skrá leikmann\n"
                "4.	Skrá viðureignir\n"
                "5.	Breyta dagsetningu á viðureign\n"
                "6.	Breyta skráningu úrslita")

            user_input = Menu_functions.menuFooter(True)

            if user_input == "1":
                self.addTournament()
            elif user_input == "2":
                self.addTeamPage()
            elif user_input == "3":
                self.addPlayer()
            elif user_input == "4":
                self.addGames()
            elif user_input == "5":
                self.changeTournamentDates()
            elif user_input == "6":
                self.changeResults()
            elif user_input == "b":
                break
            elif user_input == "q":
                Menu_functions.menuQuit()
            else:
                print("⛔ Ekki gildur valmöguleiki, reyndu aftur")
                #Menu_functions.menuExitCountdown(3, True)

    def addTeamPage(self):
        os.system('cls||clear')
        """Organizer menu for adding a team."""

        teams = self.llapi.getTeams()

        print("➢   Skrá lið:")
        print()
        team_id = len(teams) + 1
        team_name = input("o   Nafn liðs: ")
        home_address = input("o   Heimilisfang (gata og húsnúmer): ")
        club_name = input("o   Nafn félags: ")
        phone_number = Menu_functions.getPhoneNumber("o   Símanúmer: ")

        team = Team(team_id, team_name, home_address, club_name,
                    phone_number)
        self.llapi.addTeam(team)

        print("\n" + f"✅ Liðið {team_name} hefur nú verið skráð." + "\n")

        Menu_functions.menuFooter(False)

    def addTournament(self):
        os.system('cls||clear')
        """Organizer menu for adding a tournament."""
        date_list = "" + ","
        print("\n➢	Stofna deild/mót:")
        print()

        # Generate a tournament ID
        tournaments = self.llapi.getTournaments()
        tournament_id = len(tournaments) + 1

        # No two tournaments can have the same name
        tournament_name = input("o	Nafn deildar/móts: ")
        self.llapi.verifyTournament(tournament_name)

        organizer_name = input("o	Nafn Skipuleggjanda: ")
        organizer_phone = Menu_functions.getPhoneNumber(
            "o	Símanúmer skipuleggjanda: ")

        start_date, end_date = Menu_functions.getEventDates()

        tournament = Tournament(
            tournament_id, tournament_name, organizer_name, organizer_phone, start_date, end_date)
        self.llapi.addTournament(tournament)

        print(
            "\n" + f'✅ Deildin/mótið "{tournament_name}" hefur nú verið skráð.' + "\n")
        # Menu_functions.menuExitCountdown(3)

    def addPlayer(self):
        os.system('cls||clear')
        """Organizer form for player addition."""

        print(78*"_")
        print()
        print("➢   Skrá leikmann\n")

        name = input("o    Nafn: ")
        id_number = Menu_functions.getSSN("o    Kennitala: ")
        home_address = input("o    Heimilisfang (gata og húsnúmer): ")
        phone_number1 = Menu_functions.getPhoneNumber("o    GSM: ")
        phone_number2 = Menu_functions.getPhoneNumber("o    Heimasími: ")
        email = Menu_functions.getEmail("o    Netfang: ")

        the_team = self.select_team_input("\nSkrá leikmann í lið:\n")

        # les yfir og telur öll samsvarandi team_id í players og gáir hvort það er einhver skráður í liðið nú þegar. Ef nei:
        all_players = self.llapi.getPlayers()
        counter = 0
        for i in range(len(all_players)):
            if all_players[i].team_id == the_team.id:
                counter += 1

        is_captain = False
        # ef enginn er í liðinu fyrir þarf leikmaðurinn að vera skráður sem fyrirliði
        if counter == 0:
            print(
                f"\n⚠️ Enginn leikmaður hefur verið skráður í liðið {the_team.name}.\n{name} verður skráður sem fyrirliði.\n")
            confirmed = Menu_functions.getYesNo("Viltu halda áfram?")
            if not confirmed:
                return
            is_captain = True

        team_id = the_team.id

        player = Player(id_number, name, phone_number1,
                        phone_number2, email, home_address, team_id, is_captain)
        self.llapi.addPlayer(player)

        print(
            "\n" + f"✅ Leikmaðurinn {name} hefur nú verið skráður í liðið {the_team.name}." + "\n")
        # Menu_functions.menuExitCountdown(3)

    def changeTournamentDates(self):
        os.system('cls||clear')
        """Organizer form for changing dates of an existing tournament and its games"""

        # Hér þarf að sækja dagsetningar í IO sem userinn vill breyta
        print("➢	Breyta dagsetningu á viðureign: ")
        print()

        the_tournament = self.select_tournament_input()

        print(f"Breyta dagsetningu fyrir {the_tournament.name}:")
        start_date, end_date = Menu_functions.getEventDates()
        updated_tournament = Tournament(the_tournament.id, the_tournament.name,
                                        the_tournament.organizer_name, the_tournament.organizer_phone, start_date, end_date)
        self.llapi.changeDateTournament(updated_tournament)
        os.system('cls||clear')
        selection = None
        while selection == None:
            game = self.select_game_input_upcoming(updated_tournament.id)
            date = Menu_functions.getDate("\no       Sláðu inn nýja dagsetningu (dd.mm.yy): ")
            updated_game = Game(game.id, updated_tournament.id, game.home_team, game.away_team, date, game.results_hometeam, game.results_awayteam)
            self.llapi.changeDateGame(updated_game)
            userinput = input("\nViltu breyta dagsetning á öðrum leik? \n\ny. Já \nn. Nei\n\n ")
            if userinput != "y":
                selection = 1

        user_input = Menu_functions.menuFooter(True)
        return user_input

    def addGames(self):
        os.system('cls||clear')
        print("\nSkrá viðureignir: ")

        tournament = self.select_tournament_input()

        while True:
            date = Menu_functions.getDate(
                "\no	Dagsetning viðureignar (dd.mm.áá): ")
            is_valid = Menu_functions.isBetweenDates(
                date, tournament.start_date, tournament.end_date)
            if is_valid:
                break

        home_team = self.select_team_input("\n🏠 Veljið heimalið:\n")

        is_valid = False
        while not is_valid:
            away_team = self.select_team_input("\n🚌 Veljið útilið: \n")
            if home_team.id is not away_team.id:
                break
            else:
                print("\n\n⛔ Ógilt val! Ekki má velja sama lið tvisvar. Reynið aftur.")

        games = self.llapi.getGames()
        game_id = len(games)+1

        game = Game(game_id, tournament.id,
                    home_team.name, away_team.name, date)
        self.llapi.addGame(game)

        print(
            f"\n ✅ Viðureign '{home_team.name} vs. {away_team.name}' hefur verið bætt við.\n")

    def select_tournament_input(self):
        os.system('cls||clear')
        """Prints a numbered list of all tournaments and asks the user for their selection. The selected tournament index is returned"""
        print("\nVeljið mót:\n")
        tournaments = self.llapi.getTournaments()
        command = ""
        while True:
            for i in range(len(tournaments)):
                print(
                    i+1, ". ", f"{tournaments[i].name:<20}", f"🗓️:  {tournaments[i].start_date} - {tournaments[i].end_date}")
            try:
                command = int(
                    input(f"\nVeldu mót af listanum hér fyrir ofan (sláðu t.d. inn 1 fyrir {tournaments[0].name}): "))
                if command < 1 or command > len(tournaments):
                    print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")
                    continue
                break
            except ValueError:
                print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")
        return tournaments[command-1]

    def select_team_input(self, ui_str):
        os.system('cls||clear')
        """Prints a numbered list of all teams and asks the user for their selection. The selected team index is returned"""
        print(ui_str)
        teams = self.llapi.getTeams()
        command = ""
        while True:
            for i in range(len(teams)):
                print(i+1, ". ", teams[i].name)
            try:
                command = int(
                    input(f"\nVeldu lið af listanum hér fyrir ofan (sláðu t.d. inn 1 fyrir {teams[0].name}): "))
                if command < 1 or command > len(teams):
                    print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")
                    continue
                break
            except:
                print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")

        return teams[command-1]

    def Skraning_Game_Print(self, type):
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

    def changeResults(self):
        os.system('cls||clear')
        """ Allows the organizer to change the results of a previous game"""
        tournament = OrganizerUI.select_tournament_input(self)
        os.system('cls||clear')
        game = self.select_game_input_finished(tournament.id)

        home_team_id = self.llapi.getTeam_id(game.home_team)
        away_team_id = self.llapi.getTeam_id(game.away_team)
        
        home_players = self.llapi.getPlayersFromTeam(home_team_id)
        away_players = self.llapi.getPlayersFromTeam(away_team_id)

        resultlist = []
        exclude = []
        # allar 501 1v1 umferðirnar, niðurstöður:
        result_501_1v1_1 = self.get_501_1v1_results(home_team_id, away_team_id, [])
        for player in result_501_1v1_1.home_players:
            exclude.append(player.playerid)
        for player in result_501_1v1_1.away_players:
            exclude.append(player.playerid)
        result_501_1v1_2 = self.get_501_1v1_results(home_team_id, away_team_id, exclude)
        for player in result_501_1v1_2.home_players:
            exclude.append(player.playerid)
        for player in result_501_1v1_2.away_players:
            exclude.append(player.playerid)
        result_501_1v1_3 = self.get_501_1v1_results(home_team_id, away_team_id, exclude)
        for player in result_501_1v1_3.home_players:
            exclude.append(player.playerid)
        for player in result_501_1v1_3.away_players:
            exclude.append(player.playerid)
        result_501_1v1_4 = self.get_501_1v1_results(home_team_id, away_team_id, exclude)
        resultlist.append(result_501_1v1_1)
        resultlist.append(result_501_1v1_2)
        resultlist.append(result_501_1v1_3)
        resultlist.append(result_501_1v1_4)

        # niðurstaða 301 umferðarinnar:
        os.system('cls||clear')
        result_301_2v2 = self.get_301_results(home_team_id, away_team_id)
        resultlist.append(result_301_2v2)

        # niðurstaða cricket:
        exclude = []
        for player in result_301_2v2.home_players:
            exclude.append(player.playerid)
        for player in result_301_2v2.away_players:
            exclude.append(player.playerid)
        result_cricket = self.get_cricket_results(home_team_id, away_team_id, exclude)
        resultlist.append(result_cricket)

        # niðurstaða 501 4v4 umferðarinnar:
        os.system('cls||clear')
        result_501_4v4 = self.get_501_4v4_results(home_team_id, away_team_id)
        resultlist.append(result_501_4v4)

        playerscores = []
        for player in home_players:
            playerscores.append(PlayerScore(tournament.id, game.id, player.playerid))
        for player in away_players:
            playerscores.append(PlayerScore(tournament.id, game.id, player.playerid))

        # Stigagjöf - QPs, Innskot og Útskot
        os.system('cls||clear')
        playerscores = self.getPlayerScores(playerscores)

        teams = [TeamScore(home_team_id, tournament.id, game.id), TeamScore(away_team_id, tournament.id, game.id)]
        gameslist = self.llapi.getUpcomingGames()
        self.llapi.addResults(teams, playerscores, resultlist, game, gameslist)

        print("√ Niðurstöður skráðar!")
        

    def get_501_1v1_results(self, home_team_id, away_team_id, exclude_ids):
        os.system('cls||clear')
        self.Skraning_Game_Print("501s")
        home_player = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, exclude_ids)
        os.system('cls||clear')
        self.Skraning_Game_Print("501s")
        away_player = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, exclude_ids)

        home_score = 0
        away_score = 0
        counter = 1
        while home_score < 2 and away_score < 2:
            os.system('cls||clear')
            self.Skraning_Game_Print("501s")
            new_home_score, new_away_score = self.who_won(home_player.name,away_player.name, counter)
            home_score += new_home_score
            away_score += new_away_score
            counter += 1

        return GameResult("501 1v1", [home_player], [away_player], home_score, away_score)

    def get_301_results(self, home_team_id, away_team_id):
        self.Skraning_Game_Print("301")
        home_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id)
        os.system('cls||clear')
        self.Skraning_Game_Print("301")
        home_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid])
        os.system('cls||clear')
        self.Skraning_Game_Print("301")
        away_player1 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id)
        os.system('cls||clear')
        self.Skraning_Game_Print("301")
        away_player2 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, [away_player1.playerid])
        os.system('cls||clear')

        home_score = 0
        away_score = 0
        counter = 1
        while home_score < 2 and away_score < 2:
            os.system('cls||clear')
            self.Skraning_Game_Print("301")
            new_home_score, new_away_score = self.who_won(self.llapi.getTeamNameFromId(home_team_id), self.llapi.getTeamNameFromId(away_team_id), counter)
            home_score += new_home_score
            away_score += new_away_score
            counter += 1

        return GameResult("301 2v2", [home_player1, home_player2], [away_player1, away_player2], home_score, away_score)

    def get_cricket_results(self, home_team_id, away_team_id, exclude_ids):
        os.system('cls||clear')
        self.Skraning_Game_Print("C")
        home_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, exclude_ids)
        os.system('cls||clear')
        self.Skraning_Game_Print("C")
        exclude_ids.append(home_player1.playerid)
        home_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, exclude_ids)
        os.system('cls||clear')
        self.Skraning_Game_Print("C")
        away_player1 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, exclude_ids)
        os.system('cls||clear')
        self.Skraning_Game_Print("C")
        exclude_ids.append(away_player1.playerid)
        away_player2 = self.select_teamplayer_input(
            "\nVeljið útileikmann\n", away_team_id, exclude_ids)
        os.system('cls||clear')

        home_score = 0
        away_score = 0
        counter = 1
        while home_score < 2 and away_score < 2:
            os.system('cls||clear')
            self.Skraning_Game_Print("301")
            new_home_score, new_away_score = self.who_won(self.llapi.getTeamNameFromId(home_team_id), self.llapi.getTeamNameFromId(away_team_id), counter)
            home_score += new_home_score
            away_score += new_away_score
            counter += 1

        return GameResult("Cricket 2v2", [home_player1, home_player2], [away_player1, away_player2], home_score, away_score)

    def get_501_4v4_results(self, home_team_id, away_team_id):
        self.Skraning_Game_Print("501f")
        home_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id)
        os.system('cls||clear')
        self.Skraning_Game_Print("501f")
        home_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid])
        os.system('cls||clear')
        self.Skraning_Game_Print("501f")
        home_player3 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid, home_player2.playerid])
        os.system('cls||clear')
        self.Skraning_Game_Print("501f")
        home_player4 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", home_team_id, [home_player1.playerid, home_player2.playerid, home_player3.playerid])
        os.system('cls||clear')
        self.Skraning_Game_Print("501f")
        away_player1 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", away_team_id)
        os.system('cls||clear')
        self.Skraning_Game_Print("501f")
        away_player2 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", away_team_id, [away_player1.playerid])
        os.system('cls||clear')
        self.Skraning_Game_Print("501f")
        away_player3 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", away_team_id, [away_player1.playerid, away_player2.playerid])
        os.system('cls||clear')
        self.Skraning_Game_Print("501f")
        away_player4 = self.select_teamplayer_input(
            "\nVeljið heimaleikmann\n", away_team_id, [away_player1.playerid, away_player2.playerid, away_player3.playerid])
        os.system('cls||clear')


        home_score = 0
        away_score = 0
        counter = 1
        while home_score < 2 and away_score < 2:
            os.system('cls||clear')
            self.Skraning_Game_Print("501f")
            new_home_score, new_away_score = self.who_won(self.llapi.getTeamNameFromId(home_team_id), self.llapi.getTeamNameFromId(away_team_id), counter)
            home_score += new_home_score
            away_score += new_away_score
            counter += 1

        return GameResult("501 4v4", [home_player1, home_player2, home_player3, home_player4], [away_player1, away_player2, away_player3, away_player4], home_score, away_score)

    def getPlayerScores(self, playerscores):
        for playerscore in playerscores:
            os.system('cls||clear')
            self.Skraning_Game_Print("score")
            print(f"Stigagjöf fyrir {self.llapi.getPlayerNameFromId(playerscore.playerid)}: ")
            playerscore.QPs = input("Hversu mörg Quality Points fékk leikmaðurinn? - 0 ef engin: ")
            playerscore.inshots = input("Hvað var hæsta innskotið hjá leikmanninum?: ")
            playerscore.outshots = input("Hvað var hæsta útskot hjá leikmanninum?: ")
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
        #print("a. heimalið")
        #print("b. útilið\n")

        while True:
            print(f"Hver vann {counter}. umferð?\n")
            print(f"a. {home_player}")
            print(f"b. {away_player}")
            user_input = input(
                "Sláðu inn valmöguleika af listanum hér að ofan: ")
            if user_input == "a":
                return (1, 0)
            if user_input == "b":
                return (0, 1)
            print('⛔ Ekki gildur valmöguleiki, reyndu aftur')


    def select_game_input_finished(self, tournament_id):
        os.system('cls||clear')
        """Prints a numbered list of all games and asks the user for their selection. The selected game index is returned"""

        print(f"\nBreyta Niðurstöðu\n\nVeljið viðureign:\n")
        games_upcoming = self.llapi.getGamesFinished()
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

        return games_upcoming_in_tournament[command-1]

    def select_game_input_upcoming(self, tournament_id):
        os.system('cls||clear')
        """Prints a numbered list of all games and asks the user for their selection. The selected game index is returned"""

        print(f"\nBreyta Dagsetningu\n\nVeljið viðureign:\n")
        games_upcoming = self.llapi.getUpcomingGames()
        games_upcoming_in_tournament = [
            game for game in games_upcoming if game.tournament_id == tournament_id]
        while True:
            for i, game in enumerate(games_upcoming_in_tournament):
                print(f"{i+1}. {game.date} | {game.home_team} vs. {game.away_team}")
            try:
                command = int(
                    input(f"\nVeldu viðureign af listanum hér fyrir ofan (sláðu inn tölustafinn á viðureigninni sem þú vilt velja): "))
                if command < 1 or command > len(games_upcoming_in_tournament):
                    print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")
                    continue
                break
            except ValueError:
                print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")

        return games_upcoming_in_tournament[command-1]
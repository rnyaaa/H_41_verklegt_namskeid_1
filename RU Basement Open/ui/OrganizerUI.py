from logic.LL_API import LL_API
from models.game import Game
from models.player import Player
from models.team import Team
from models.tournament import Tournament
from ui.UI import Menu_functions


class OrganizerUI():

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayOrganizerMenu(self):
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
        """Organizer form for changing dates of an existing tournament."""

        # Hér þarf að sækja dagsetningar í IO sem userinn vill breyta
        print("➢	Breyta dagsetningu á viðureign: ")
        print()

        the_tournament = self.select_tournament_input()

        print(f"Breyta dagsetningu fyrir {the_tournament.name}:")

        start_date, end_date = Menu_functions.getEventDates()

        updated_tournament = Tournament(the_tournament.id, the_tournament.name,
                                        the_tournament.organizer_name, the_tournament.organizer_phone, start_date, end_date)

        self.llapi.changeDate(updated_tournament)

        user_input = Menu_functions.menuFooter(True)
        return user_input

    def addGames(self):
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

    def changeResults(self):
        print("➢	Breyta skráningu úrslita:\n")
        selected_tournament = self.select_tournament_input()

        all_results = self.llapi.getResults()
        for result in all_results:
            for list in result:
                if selected_tournament.id == list.id:
                    print(f"{list.team} {list.winningscore}")
        print()

        # print(hér kemur tafla með úrslitum )

        user_input = Menu_functions.menuFooter(True)
        return user_input

    def select_tournament_input(self):
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

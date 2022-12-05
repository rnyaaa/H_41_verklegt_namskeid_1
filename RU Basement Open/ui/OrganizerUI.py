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
                "2.	Skrá leikmann\n"
                "3.	Skrá lið\n"
                "4.	Skrá viðureignir\n"
                "5.	Breyta dagsetningu á viðureign\n"
                "6.	Breyta skráningu úrslita")

            user_input = Menu_functions.menuFooter(True)

            if user_input == "1":
                self.addTournament()
            elif user_input == "2":
                self.addPlayer()
            elif user_input == "3":
                self.addTeamPage()
            elif user_input == "4":
                self.addGames()
            elif user_input == "5":
                self.changeResults
            elif user_input == "6":
                self.changeResults()
            elif user_input == "b":
                break
            elif user_input == "q":
                Menu_functions.menuQuit()
            else:
                print("Ekki gildur valmöguleiki, reyndu aftur")
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

        games_won = 0
        rounds_won = 0

        team = Team(team_id, team_name, home_address, club_name,
                    phone_number, games_won, rounds_won)
        self.llapi.addTeam(team)

        print("\n" + f"Liðið {team_name} hefur nú verið skráð." + "\n")

    def addTournament(self):
        """Organizer menu for adding a tournament."""
        date_list = "" + ","
        print("➢	Stofna deild/mót:")
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

        start_date = Menu_functions.getDate("o	Byrjunardagsetning deildar (dd.mm.yy): ")

        print(f"\no	Nær deildin/mótið yfir meira en einn dag ({start_date})?\n")
        print("y. Já" + "\n" + "n. nei\n")
        is_multiple_days = input("Sláðu inn val þitt: ")
        ask_y_n = True
        while ask_y_n:
            try:
                if is_multiple_days.lower() == "n":
                    end_date = start_date
                    ask_y_n = False
                if is_multiple_days.lower() == "y":
                    end_date = Menu_functions.getDate("o	Lokadagsetning deildar (dd.mm.yy): ")
                    ask_y_n = False
                else:
                    return ValueError
            except ValueError:
                print("Ekki gildur valmöguleiki, reyndu aftur")
        
        tournament_type = Menu_functions.getTournamentType("o	ZZZZZZZZZZZZZZZZZZZZZZZZZZ:")


        tournament = Tournament(
            tournament_id, tournament_name, organizer_name, organizer_phone, date_list)
        self.llapi.addTournament(tournament)

        print(
            "\n" + f'Deildin/mótið "{tournament_name}" hefur nú verið skráð.' + "\n")
        # Menu_functions.menuExitCountdown(3)

    def select_team_input(self):
        print("\nSkrá leikmann í lið:\n")
        teams = self.llapi.getTeams()
        command = ""
        while True:
            for i in range(len(teams)):
                print(i+1, ". ", teams[i].name)
            command = int(
                input(f"\nVeldu lið af listanum hér fyrir ofan (sláðu t.d. inn 1 fyrir {teams[0].name}): "))
            if command < 1 or command > len(teams):
                print("\nEkki gildur valmöguleiki, reyndu aftur.\n")
                continue
            break
        return teams[i]

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

        the_team = self.select_team_input()

        team_id = the_team.id

        player = Player(id_number, name, phone_number1,
                        phone_number2, email, home_address, team_id)
        self.llapi.addPlayer(player)

        print(
            "\n" + f"Leikmaðurinn {name} hefur nú verið skráður í liðið {the_team.name}." + "\n")
        # Menu_functions.menuExitCountdown(3)

    def changeTournamentDates(self):
        """Organizer form for changing dates of an existing tournament."""

        # Hér þarf að sækja dagsetningar í IO sem userinn vill breyta
        print("➢	Breyta dagsetningu á viðureign: ")
        print()
        name = input("Nafn móts: ")
        print()

        # print(hér koma viðureignirnar)
        print()

        user_input = Menu_functions.menuFooter(True)
        return user_input

    def addGames(self):

        print("\nSkrá viðureignir: ")
        while True:
            tournament = input("\no	Mót: ")
            date = input("o	Dagsetning viðureignar (dd.mm.áá): ")
            if date == "":
                break
            else:
                home_away = input("o	Hverjir keppa? (Heimalið - útilið): ")
                Game(tournament, home_away, date)

    def changeResults(self):
        # Hér þarf að sækja úrslit í IO sem userinn vill breyta
        print("➢	Breyta skráningu úrslita: ")
        all_results = self.llapi.getResults()
        for result in all_results:
            for list in result:
                print(list.game_id)
        print()
        name = input("	Nafn móts: ")
        print()

        # print(hér kemur tafla með úrslitum )

        user_input = Menu_functions.menuFooter(True)
        return user_input

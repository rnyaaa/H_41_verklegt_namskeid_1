from logic.LL_API import LL_API
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

                "1.	Skrá lið\n"
                "2.	Stofna deild\n"
                "3.	Skrá leikmenn\n"
                "4.	Breyta dagsetningu á viðureign\n"
                "5.	Breyta skráningu úrslita")

            user_input = Menu_functions.menuFooter(True)

            if user_input == "1":
                self.addTeamPage()
            elif user_input == "2":
                self.addTournament()
            elif user_input == "3":
                self.addPlayer()
            elif user_input == "4":
                self.changeTournamentDates()
            elif user_input == "5":
                self.changeResults()
            elif user_input == "b":
                break
            elif user_input == "q":
                Menu_functions.menuQuit()
            else:
                print("Ekki gildur valmöguleiki, reyndu aftur")
                Menu_functions.menuExitCountdown(3, True)

    def addTeamPage(self):
        """Organizer menu for adding a team."""

        print("➢   Skrá lið:")
        print()
        team_id = input("o  Númer liðs: ")
        team_name = input("o   Nafn liðs: ")
        home_address = input("o   Heimilisfang: ")
        club_name = input("o   Nafn félags: ")
        phone_number = LL_API.isPhoneNumber("o   Símanúmer")

        team = Team(team_id, team_name, home_address, club_name, phone_number)
        self.llapi.addTeam(team)

    def addTournament(self):
        """Organizer menu for adding a tournament."""
        date_list = "" + ","
        print("➢	Stofna deild:")
        print()

        # Tvær eða fleiri deildir mega ekki deila sama nafni
        tournament_name = input("o	Nafn deildar: ")
        self.llapi.verifyTournament(tournament_name)

        organizer_name = input("o	Nafn Skipuleggjanda: ")
        organizer_phone = LL_API.isPhoneNumber(
            "o	Símanúmer skipuleggjanda: ")

        while True:
            date = input("o	Dagsetning viðureignar: ")
            if date == "":
                break
            else:
                date_list += date

        tournament = Tournament(
            tournament_name, organizer_name, organizer_phone, date_list)
        self.llapi.addTournament(tournament)

        print("\n" + f"{tournament_name} hefur nú verið skráð." + "\n")
        Menu_functions.menuExitCountdown(3)
        

    def addPlayer(self):
        """Organizer form for player addition."""

        print(78*"_")
        print()
        print("➢   Skrá leikmann\n")
        name = input("o    Nafn: ")
        id_number = input("o    Kennitala: ")
        home_address = input("o     Heimilisfang: ")
        phone_number1 = LL_API.isPhoneNumber("o    GSM: ")
        phone_number2 = LL_API.isPhoneNumber("o    Heimasími: ")
        email = input("o    Netfang: ")
        registered_team = input(
            f"Liðið sem leikmaðurinn tilheyrir:\n"
            # Hér kemur listi af liðum sem hafa verið skráð/á eftir að útfæra
        )
        player = Player(id_number, name, phone_number1,
                        phone_number2, email, home_address)
        self.llapi.addPlayer(player)

        print("\n" + f"Leikmaðurinn {name} hefur nú verið skráður." + "\n")
        Menu_functions.menuExitCountdown(3)

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

    def changeResults(self):
        # Hér þarf að sækja úrslit í IO sem userinn vill breyta
        print("➢	Breyta skráningu úrslita: ")
        print()
        name = input("	Nafn móts: ")
        print()

        # print(hér kemur tafla með úrslitum )

        user_input = Menu_functions.menuFooter(True)
        return user_input

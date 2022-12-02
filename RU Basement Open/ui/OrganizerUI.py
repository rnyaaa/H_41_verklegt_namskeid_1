from logic.LL_API import LL_API
from models.player import Player
from models.team import Team
<<<<<<< HEAD
from models.tournament import Tournament
from ui.UI import Menu_prompt
=======
from ui.UI import Menu_functions
>>>>>>> 50a315cdd8210737b39d4c6f37b93c7b150a176a


class OrganizerUI():

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayOrganizerMenu(self):
        """Displays the organizer submenu."""
        while True:
            print(78*"_")
            print()
            print(
                "Velkominn, mótshaldari!\n"
                "\n"
                "➢  Valmynd:\n"
                "\n"
                "1.	Skrá lið\n"
                "2.	Stofna deild\n"
                "3.	Skrá leikmann\n"
                "4.	Breyta dagsetningu á viðureign\n"
                "5.	Breyta skráningu úrslita\n")

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
            else:
                # Á eftir að útfæra loopu
                ("Ekki gildur valmöguleiki, reyndu aftur")

    def addPlayer(self):
        """Organizer player addition form."""
        # Fyrir hvern leikmann þarf að skrá nafn, kennitölu, heimilisfang, heimasíma,
        # GSM-síma, netfang og í hvaða liði hann spilar.
        print(78*"_")
        print()
        print("➢   Skrá leikmann\n")
        name = input("o    Nafn: ")
        id_number = input("o    Kennitala: ")
<<<<<<< HEAD
        home_address = input("o     Heimilisfang: ")
        phone_number1 = LL_API.isPhoneNumber("o    GSM: ")
        phone_number2 = LL_API.isPhoneNumber("o    Heimasími: ")
        #email = input("o    Netfang: ")
=======
        home_address = input("o    Heimilisfang: ")
        phone_number1 = input("o    GSM: ")
        phone_number2 = input("o    Heimasími: ")
        email = input("o    Netfang: ")
>>>>>>> 50a315cdd8210737b39d4c6f37b93c7b150a176a
        registered_team = input(
            f"Liðið sem leikmaðurinn tilheyrir:\n"
            # Hér kemur listi af liðum sem hafa verið skráð/á eftir að útfæra
        )
        player = Player(id_number, name, phone_number1,
                        phone_number2, email, home_address)
        self.llapi.addPlayer(player)

        print("\n" + f"Leikmaðurinn {name} hefur nú verið skráður." + "\n")
        Menu_functions.menuExitCountdown(3)

    def addTeamPage(self):
        print("➢   Skrá lið:")
        print()
<<<<<<< HEAD
        team_id = input("o  Númer liðs: ") 
        team_name = input("o   Nafn liðs: ")
        home_address = input("o   Heimilisfang: ")
        club_name = input("o   Nafn félags: ")
        phone_number = LL_API.isPhoneNumber("o   Símanúmer")
        
=======
        # Á þetta að vera kennitala eða númer?
        team_id = input("o    Kennitala liðs: ")
        team_name = input("o    Nafn liðs: ")
        home_address = input("o    Heimilisfang: ")
        club_name = input("o    Nafn félags: ")
        phone_number = input("o    Símanúmer: ")

>>>>>>> 50a315cdd8210737b39d4c6f37b93c7b150a176a
        # MUNA AÐ LAGA ÞETTA - INTEGRATE-A OG LÁTA LL API SJÁ UM
        team = Team(team_id, team_name, home_address, club_name, phone_number)
        self.llapi.addTeam(team)

        print("\n" + f"Liðið {team_name} hefur nú verið skráð." + "\n")
        Menu_functions.menuExitCountdown(3)

    def addTournament(self):
        print("➢	Stofna deild:") 
        print()
        while True:
<<<<<<< HEAD
            tournament_name = input("o	Nafn deildar: ") # Tvær eða fleiri deildir meiga ekki deila sama nafni
            data = self.llapi.getTournaments()
            for list in data:
                if list[0] == tournament_name:
                    print("Nafnið er frátekið, reyndu aftur.")
                else:
                    break 
            organizer_name = input("o	Nafn Skipuleggjanda: ")
            organizer_phone = LL_API.isPhoneNumber("o	Símanúmer skipuleggjanda: ")
            tournament_type = input("o	Tegund móts: ")
            
            tournament = Tournament(tournament_name, organizer_name, organizer_phone, tournament_type)
            self.llapi.addTournament(tournament)
        
     
=======
            dates = input("o	Dagsetningar: ")
            if dates == "":
                break
        raise NotImplementedError()
        # Má gera lista að ofan til að geyma dagsetingar?
        # MUNA AÐ LAGA ÞETTA - INTEGRATE-A OG LÁTA LL API SJÁ UM
        # LL_API.addTournament(tournament_name, organizer_name,
        # organizer_number, tournament_type, dates)
>>>>>>> 50a315cdd8210737b39d4c6f37b93c7b150a176a

    def addTournamentDates():
        name = input("Nafn mótar: ")
        while True:
            date = input("Dagsetningar mótsins: ") # Á eftir að útfæra 

    
    def changeTournamentDates(self):
        # Hér þarf að sækja dagsetningar í IO sem userinn vill breyta
        print("➢	Breyta dagsetningu á viðureign: ")
        print()
<<<<<<< HEAD
        name = input("Nafn mótar: ")
=======
        print("     Veldu viðureign:\n")
>>>>>>> 50a315cdd8210737b39d4c6f37b93c7b150a176a
        print()

        # print(hér koma viðureignirnar)
        print()

        user_input = Menu_functions.menuFooter(True)
        return user_input

    def changeResults(self):
        # Hér þarf að sækja úrslit í IO sem userinn vill breyta
        print("➢	Breyta skráningu úrslita: ")
        print()
        print("	Veldu úrslit: ")
        print()

        # print(hér kemur tafla með úrslitum )

        user_input = Menu_functions.menuFooter(True)
        return user_input

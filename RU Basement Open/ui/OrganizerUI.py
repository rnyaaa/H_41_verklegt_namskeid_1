from logic.LL_API import LL_API
from ui.UI import Menu_prompt


class OrganizerUI():

    def displayOrganizerMenu():
        """Displays the organizer submenu."""

        print(78*"_")
        print()
        print(
            "Velkominn, mótshaldari!\n"
            "\n"
            "➢  Valmynd:\n"
            "\n"
            "1.	Skrá lið\n"
            "2.	Stofna deild\n"
            "3.	Skrá leikmenn\n"
            "4.	Breyta dagsetningu á viðureign\n"
            "5.	Breyta skráningu úrslita\n"
            "b. Til baka\n")

        user_input = Menu_prompt.menuFooter(True)
        while True:
            if user_input == "1":
                OrganizerUI.addTeamPage()
            elif user_input == "2":
                OrganizerUI.addTournament()
            elif user_input == "3":
                OrganizerUI.addPlayer()
            elif user_input == "4":
                OrganizerUI.changeTournamentDates()
            elif user_input == "5":
                OrganizerUI.changeResults()
            elif user_input == "b" or "B":
                break
            else:
                ("Ekki gildur valmöguleiki, reyndu aftur") # Á eftir að útfæra loopu

    def addPlayer():
        """Organizer player addition form."""

        print("➢   Skrá leikmenn")
        name = input("o Nafn: ")
        id_number = input("o    Kennitala: ")
        home_address = input("o     Heimilisfang: ")
        phone_number1 = input("o    GSM: ")
        phone_number2 = input("o    Heimasími: ")
        #email = input("o    Netfang: ")
        registered_team = input(
            f"Liðið sem leikmaðurinn tilheyrir:\n"
            # Hér kemur listi af liðum sem hafa verið skráð/á eftir að útfæra
        )
        LL_API.addPlayer(name, id_number, home_address,
                         phone_number1, phone_number2, registered_team)

    def addTeamPage():
        print("➢   Skrá lið:")
        print()
        team_name = input("o   Nafn liðs: ")
        home_address = input("o   Heimilisfang: ")
        team_organiser = input("o   Nafn félags: ")
        phone_number = input("o   Símanúmer: ")

        # MUNA AÐ LAGA ÞETTA - INTEGRATE-A OG LÁTA LL API SJÁ UM
        LL_API.addTeam(team_name, home_address, team_organiser, phone_number)

    def addTournament():
        print("➢	Stofna deild:")
        print()
        tournament_name = input("o	Nafn deildar: ")
        organizer_name = input("o	Nafn Skipuleggjanda: ")
        organizer_number = input("o	Símanúmer skipuleggjanda: ")
        tournament_type = input("o	Tegund móts: ")
        while True:
            dates = input("o	Dagsetningar: ")
            if dates == "":
                break

        # Má gera lista að ofan til að geyma dagsetingar?
        # MUNA AÐ LAGA ÞETTA - INTEGRATE-A OG LÁTA LL API SJÁ UM
        LL_API.addTournament(tournament_name, organizer_name,
                             organizer_number, tournament_type, dates)

    def changeTournamentDates():
        print("➢	Breyta dagsetningu á viðureign: \n") # Hér þarf að sækja dagsetningar í IO sem userinn vill breyta
        print()
        print("     Veldu viðureign\n")
        print()
        # print(hér koma viðureignirnar)
        print()

        user_input = Menu_prompt.menuFooter(True)
        return user_input

    def changeResults():
        print("➢	Breyta skráningu úrslita:\n ") # Hér þarf að sækja úrslit í IO sem userinn vill breyta
        print()
        print("	Veldu úrslit: ")
        print()

        # print(hér kemur tafla með úrslitum )

        user_input = Menu_prompt.menuFooter(True)
        return user_input
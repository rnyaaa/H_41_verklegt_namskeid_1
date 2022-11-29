from ui.UI import Main_Menu, OrganizerUI



user_input = Main_Menu.displayMainMenu()
if user_input == "1":
    selection = Main_Menu.openOrganizerMenu()
    if selection == "1":
        OrganizerUI.addTeamPage()
    elif selection == "2":
        OrganizerUI.addTournament()
    elif selection == "3":
        OrganizerUI.addPlayer()
    elif selection == "4":
        OrganizerUI.changeTournamentDates()
    elif selection == "5":
        OrganizerUI.changeResults()
    else:
        ("Ekki gildur valmöguleiki!") # Á eftir að útfæra loopu

elif user_input == "2":
    selection = Main_Menu.openCaptainMenu()

elif user_input == "3":
    Main_Menu.openShowGamesMenu()

elif user_input == "4":
    Main_Menu.openViewerMenu()

elif user_input.lower() == "q":
    print()
    print("Bless 🥲")
    print()
    print("""
        .--'''''''''--.
     .'      .---.      '.
    /    .-----------.    \
   /        .-----.        \
   |       .-.   .-.       |
   |      /   \ /   \      |
    \    | .-. | .-. |    /
     '-._| | | | | | |_.-'
         | '-' | '-' |
          \___/ \___/
       _.-'  /   \  `-._
     .' _.--|     |--._ '.
     ' _...-|     |-..._ '
            |     |
            '.___.'
              """)
    quit()
else: 
    print("Ekki gildur valmöguleiki! Reyndu aftur") # Á eftir að útfæra loopu

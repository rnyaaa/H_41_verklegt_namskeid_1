from ui.UI import Main_Menu, OrganizerUI



user_input = Main_Menu.displayMainMenu()
if user_input == "1":
    Main_Menu.openOrganizerMenu()
elif user_input == "2":
    selection = Main_Menu.openCaptainMenu()
    if selection == "1":
        OrganizerUI.addTeamPage()
    elif selection == "2":
        OrganizerUI.addTournament
elif user_input == "3":
    Main_Menu.openShowGamesMenu()
elif user_input == "4":
    Main_Menu.openViewerMenu()
elif user_input.lower() == "q":
    print()
    print("Bless 🥲")
    quit()
else: 
    print("Ekki gildur valmöguleiki! Reyndu aftur")
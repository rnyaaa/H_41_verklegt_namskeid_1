from ui.UI import Main_Menu, OrganizerUI
from ui.UI import CaptainUI
from ui.Main_menu_ui import Main_Menu_UI

mainmenu = Main_Menu_UI()
mainmenu.input_prompt()




# Þetta má taka út, erum búin að implementa í Main_menu_ui.py
"""user_input = Main_Menu.displayMainMenu()
if user_input == "1":
    selection = OrganizerUI.openOrganizerMenu()
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
    selection = CaptainUI.openCaptainMenu()


elif user_input == "3":
    Main_Menu.openShowGamesMenu()

elif user_input == "4":
    Main_Menu.openViewerMenu()

elif user_input.lower() == "q":
    print()
    print("Bless 🥲"
    quit()
else: 
    print("Ekki gildur valmöguleiki! Reyndu aftur") # Á eftir að útfæra loopu"""

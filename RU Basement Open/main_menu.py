from ui.UI import Main_Menu


ui = Main_Menu()
user_input = ui.displayMainMenu()
if user_input == "1":
    ui.openOrganizerMenu()
elif user_input == "2":
    ui.openCaptainMenu()
elif user_input == "3":
    ui.openShowGamesMenu()
elif user_input == "4":
    ui.openViewerMenu()
elif user_input == "q":
    quit()
else: 
    ("Ekki gildur valmöguleiki! Reyndu aftur")
from logic.LL_API import LL_API
from ui.UI import Menu_functions
from ui.OrganizerUI import OrganizerUI
import datetime
import time

class ShowGamesUI():

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def showGamesPage(self):
        """Displays game overview menu."""
        while True:
            print(78*"_")
            print()
            print(
                "➢  Valmynd:\n"
                "\n"
                "1.	Listi yfir komandi viðureignir\n"
                "2.	Listi yfir yfirstaðnar viðureignir\n")

            user_input = Menu_functions.menuFooter(False)
            
            if user_input == "1":
                self.showTournamentDates()
            elif user_input == "2":
                self.showGames()
            elif user_input == "b":
                break
            elif user_input == "q":
                Menu_functions.menuQuit()
            else:
                print("⛔ Ekki gildur valmöguleiki, reyndu aftur")
                #Menu_functions.menuExitCountdown(3, True)

    def showTournamentDates(self):
        selected_tournament = OrganizerUI.select_tournament_input(self)
        print()
        all_games = self.llapi.getGames()
        dates_of_tournaments = self.llapi.getTournaments()


    def showGames(self):
        games = self.llapi.getGames()
        print(games.gameid)

        



    
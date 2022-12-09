from logic.LL_API import LL_API
from ui.UI import Menu_functions
from ui.OrganizerUI import OrganizerUI
import datetime
from time import time
import os

class ShowGamesUI():

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def showGamesPage(self):
        os.system('cls||clear')
        """Displays game overview menu."""
        while True:
            os.system('cls||clear')
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
                


    def showTournamentDates(self):
        os.system('cls||clear')
        games = sorted(self.llapi.getUpcomingGames(), key=lambda x: datetime.datetime.strptime(x.date, '%d.%m.%y'))   
        print()
        print("------------------------LISTI YFIR KOMANDI VIÐUREIGNIR------------------------")
        print("_"*78)
        for game in games:
            print(f"{self.llapi.getTournamentNameFromId(game.tournament_id):>20} | {game.date} | {game.home_team:>15} vs. {game.away_team:<15}")
        
        Menu_functions.menuFooter(False)

    def showGames(self):
        os.system('cls||clear')
        """
        Shows results from finished games from all competitions. 
        """
        games = self.llapi.getGamesFinished()
        print()
        print("-----------------------LISTI YFIR YFIRSTAÐNAR VIÐUREIGNIR----------------------")
        print("_"*78)
        for game in games:
            try:
                if int(game.results_hometeam) > int(game.results_awayteam):
                    print(f"{self.llapi.getTournamentNameFromId(game.tournament_id):<15} | {game.date} | {game.home_team:>15} {game.results_hometeam} vs. {game.results_awayteam} {game.away_team:<15} | Sigurvegari: {game.home_team}")
                else:
                    print(f"{self.llapi.getTournamentNameFromId(game.tournament_id):<15} | {game.date} | {game.home_team:>15} {game.results_hometeam} vs. {game.results_awayteam} {game.away_team:<15} | Sigurvegari: {game.away_team}")
            except:
                continue
        Menu_functions.menuFooter(False)
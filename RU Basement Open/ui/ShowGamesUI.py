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
        '''tournament = OrganizerUI.select_tournament_input(self)
        print()
        all_games = self.llapi.getGames()
        for game in all_games:
            if tournament.id == game.tournament_id:
                if game.results == '':
                    print(f"{game.home_team:>15} vs. {game.away_team:<15} - {game.date:>8}")
                    print()'''
                
        
        
        games = self.llapi.getUpcomingGames()
        tournament = OrganizerUI.select_tournament_input(self)
        print()
        print("             LISTI YFIR KOMANDI VIÐUREIGNIR. ")
        print()
        for game in games:
            print(f"{self.llapi.getTournamentNameFromId(game.tournament_id)} | {game.date} | {game.home_team} vs. {game.away_team}")
        
        Menu_functions.menuFooter(False)

    def showGames(self):
        games = self.llapi.getGamesFinished()
        print()
        print("             LISTI YFIR YFIRSTAÐNAR VIÐUREIGNIR. ")
        print()
        for game in games:
            if int(game.results_hometeam) > int(game.results_awayteam):
                print(f"{self.llapi.getTournamentNameFromId(game.tournament_id)} | {game.date} | {game.home_team} vs. {game.away_team} | Sigurvegari: {game.home_team} - {game.results_hometeam}/{game.results_awayteam}")
            else:
                print(f"{self.llapi.getTournamentNameFromId(game.tournament_id)} | {game.date} | {game.home_team} vs. {game.away_team} | Sigurvegari: {game.away_team} - {game.results_awayteam}/{game.results_hometeam}")
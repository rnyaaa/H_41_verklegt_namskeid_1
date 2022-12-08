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
        """
        Shows upcoming games between teams in all competitions. 
        with this format:
______________________________________________________________________________
   Coca Cola Deildin | 24.12.22 |   The lightings vs. The Anacondas  
       Pepsi deildin | 01.01.23 |   The Anacondas vs. The Oligarcs   
       Pepsi deildin | 02.01.23 |      The Brahms vs. The Rings      


        """
        '''tournament = OrganizerUI.select_tournament_input(self)
        print()
        all_games = self.llapi.getGames()
        for game in all_games:
            if tournament.id == game.tournament_id:
                if game.results == '':
                    print(f"{game.home_team:>15} vs. {game.away_team:<15} - {game.date:>8}")
                    print()'''
                
        
        
        games = self.llapi.getUpcomingGames()
        print()
        print("------------------------LISTI YFIR KOMANDI VIÐUREIGNIR------------------------")
        print("_"*78)
        for game in games:
            print(f"{self.llapi.getTournamentNameFromId(game.tournament_id):>20} | {game.date} | {game.home_team:>15} vs. {game.away_team:<15}")
        
        Menu_functions.menuFooter(False)

    def showGames(self):
        """
        Shows results from finished games from all competitions. 
        With this format. 
        ______________________________________________________________________________
       Pepsi deildin | 01.01.23 |      The Brahms 0 vs. 2 The lightings   | Sigurvegari: The lightings

        """
        games = self.llapi.getGamesFinished()
        print()
        print("------------------------LISTI YFIR YFIRSTAÐNAR VIÐUREIGNIR------------------------")
        print("_"*78)
        for game in games:
            try:
                if int(game.results_hometeam) > int(game.results_awayteam):
                    print(f"{self.llapi.getTournamentNameFromId(game.tournament_id):>20} | {game.date} | {game.home_team:>15} {game.results_hometeam} vs. {game.results_awayteam} {game.away_team:<15} | Sigurvegari: {game.home_team}")
                else:
                    print(f"{self.llapi.getTournamentNameFromId(game.tournament_id):>20} | {game.date} | {game.home_team:>15} {game.results_hometeam} vs. {game.results_awayteam} {game.away_team:<15} | Sigurvegari: {game.away_team}")
            except:
                continue
        Menu_functions.menuFooter(False)
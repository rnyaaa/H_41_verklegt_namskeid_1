from logic.LL_API import LL_API
from ui.UI import Menu_prompt


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

            user_input = Menu_prompt.menuFooter(False)
            
            if user_input == "1":
                self.showTournamentDates()
            elif user_input == "2":
                self.showGamesFinished()



    def showTournamentDates(self):
        tournament_id = input("Númer móts: ")
        print(self.llapi.getTournamentDates(tournament_id))
        

    def showGamesFinished():
        raise NotImplementedError

    def showUpcomingGames():
        raise NotImplementedError

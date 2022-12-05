from logic.LL_API import LL_API
from ui.UI import Menu_functions


class CaptainUI():

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayCaptainUI(self):
        while True:
            print(78*"_")
            print("                      ___     \n"
                  "                    /\ _ /\   \n"
                  "    >>>--->        / /\ /\ \  \n"
                  ">>>--->           |---(*)---| \n"
                  "                   \ \/_\/ /  \n"
                  "        >>>--->     \/___\/   \n"
                  "\n")
            print(
                "Velkominn, Fyrirliði.\n"
                "\n\n"
                "➢  Valmynd:\n"
                "\n"
                "1.  Skrá úrslit viðureignar")
            user_input = Menu_functions.menuFooter(True)

            if user_input == "1":
                self.addResults()
            elif user_input == "b":
                break
            elif user_input == "q":
                Menu_functions.menuQuit()
            else:
                print("Ekki gildur valmöguleiki, reyndu aftur.")
                #Menu_functions.menuExitCountdown(3, True)

            return user_input

    def addResults(self):
        tournaments = self.llapi.getTournaments()
        for list in tournaments:
            for name in list:
                print(f"{name.id}.{name.name}")
        
        gameid = input("Númer mótar: ")
        
        all_games = self.llapi.getGames()
        for game in all_games:
            for list in game:
                if list.tournament_id == gameid:
                    print(f"{list.gameid}. {list.home_team} - {list.away_team}")

        resultid = input("Númer viðureignar: ")

    







        raise NotImplementedError

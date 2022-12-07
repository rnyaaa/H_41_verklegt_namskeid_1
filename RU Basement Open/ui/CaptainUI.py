from logic.LL_API import LL_API
from ui.UI import Menu_functions
from ui.OrganizerUI import OrganizerUI


class CaptainUI():

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayCaptainUI(self):
        while True:
            print(78*"_")
            print(
                "\nVelkominn, Fyrirliði.\n"
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
                print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.")

    def addResults(self):
        tournament = OrganizerUI.select_tournament_input(self)
        tournament_name = tournament.name
        tournament_id = tournament.id

        selected_game = self.select_game_input(tournament_name, tournament_id)

        

    def select_game_input(self, tournament_name, tournament_id):
        """Prints a numbered list of all games and asks the user for their selection. The selected game index is returned"""

        print(f"\nMót/deild {tournament_name} yfirlit\nVeljið viðureign:\n")
        upcoming_games = self.llapi.getUpcomingGames()
        command = ""
        while True:
            for game in upcoming_games:
                if tournament_id == game.tournament_id:
                    print(f"{game.gameid}. {game.home_team} vs. {game.away_team}")
            try:
                command = int(
                    input(f"\nVeldu mót af listanum hér fyrir ofan (sláðu t.d. inn 1 fyrir viðureignina {upcoming_games[0].home_team} vs {upcoming_games[0].away_team}): "))
                if command < 1 or command > len(upcoming_games):
                    print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")
                    continue
                break
            except ValueError:
                print("\n⛔ Ekki gildur valmöguleiki, reyndu aftur.\n")
        return upcoming_games[command]

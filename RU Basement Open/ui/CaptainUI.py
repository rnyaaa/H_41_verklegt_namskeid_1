from logic.LL_API import LL_API
from models.playerscore import PlayerScore
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
        

        game = self.select_game_input(tournament.name, tournament.id)
        

        # Pæling um að fá lista af leikmönnum og velja númer til minnka innsláttarvillur?

        playerid = input("Veldu leikmann: ")
        result501singles_wins = input("Unnir leggir, 501 einleikur: ")
        result301_wins = input("Unnir leggir, 301 tvíleikur: ")
        resultcricket_wins = input("Unnir leggir, C tvíleikur: ")
        result501fours_wins = input("Unnir leggir, 501 fjórleikur: ")
        qps = input("Afreksstig: ")
        inshot = input("Hæsta innskotið: ")
        outshot = input("Hæsta útskotið: ")

        PlayerScore(tournament.id, game.id, playerid, qps, inshot, outshot, 
                    result501singles_wins, result301_wins, resultcricket_wins, result501fours_wins)




        

    def select_game_input(self,tournament_name, tournament_id):
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

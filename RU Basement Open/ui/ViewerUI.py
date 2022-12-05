from logic.LL_API import LL_API
from ui.UI import Menu_functions
from models.player import Player
from models.team import Team
from models.tournament import Tournament


class ViewerUI:

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayViewerUI(self):
        while True:
            print(78*"_")
            print()
            print(
                "Verið velkomin í Tölfræðivalmyndina!\n\n"

                "➢  Valmynd:\n\n"

                "1.	Listi yfir lið\n"
                "2.	Staða móts\n"
                "3.	Listi yfir þá sem hafa skorað flest afreksstig\n"
                "4.	Listi yfir þá sem eiga besta/hæsta innskotið á mótinu/deildinni\n"
                "5.	Listi yfir þá sem eiga besta/hæsta útskotið á mótinu/deildinni\n"
                "6.	Tölfræði fyrir ákveðna leikmenn")

            user_input = Menu_functions.menuFooter(False)

            if user_input == "1":
                self.showTeams()
            elif user_input == "2":
                self.showTournamentInfo()
            elif user_input == "3":
                self.showPlayerHighscoreViewer()
            elif user_input == "4":
                self.showPlayerHighscoreViewer()
            elif user_input == "5":
                self.showPlayerHighscoreViewer()
            elif user_input == "6":
                self.showPlayerStatistics()
            elif user_input == "b":
                break
            elif user_input == "q":
                Menu_functions.menuQuit()
            else:
                print("Ekki gildur valmöguleiki, reyndu aftur")
                Menu_functions.menuExitCountdown(3, True)

    def showTeams(self):
        '''Shows list of teams and their players'''
        teams = self.llapi.getTeams()
        players = self.llapi.getPlayers()
        for team in teams:
            print(f"\n{team.name}:")
            for player in players:
                if team.id == player.team_id:
                    print(f"→ {player.name:>20}")

    def showTournamentInfo(self):
        None

    def showPlayerViewer(self):
        None

    def showPlayerHighscoreViewer(self):
        pass

    def showPlayerStatistics(self):
        None

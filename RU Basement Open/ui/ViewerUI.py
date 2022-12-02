from logic.LL_API import LL_API
from ui.UI import Menu_functions


class ViewerUI:

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayViewerUI():
        while True:
            print(78*"_")
            print()
            print(
                "Verið velkomin í Tölfræðivalmyndina!\n"
                "\n"
                "➢  Valmynd:\n"
                "\n"
                "1.	Listi yfir lið\n"
                "2.	Staða móts\n"
                "3.	Listi yfir þá sem hafa skorað flest afreksstig\n"
                "4.	Listi yfir þá sem eiga besta/hæsta innskotið á mótinu/deildinni\n"
                "5.	Listi yfir þá sem eiga besta/hæsta útskotið á mótinu/deildinni\n"
                "6.	Tölfræði fyrir ákveðna leikmenn")

            user_input = Menu_functions.menuFooter(False)
            return user_input

    def showTournamentInfo():
        None

    def showTeams():
        '''Shows list of teams and their players'''

        print(">	Birta lista yfir Liðum\n")
        result = LL_API.getTeams()
        for name in result:
            print(f"{name[0]}:")
            print(f"{name[6]:>6}:")
            print(f"{name[7]:>6}:")
            print(f"{name[8]:>6}:")
            print(f"{name[9]:>6}:")
            print()

        user_input = Menu_functions.menuFooter(False)

    def showPlayerViewer():
        None

    def showPlayerHighscoreViewer():
        None

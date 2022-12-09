from logic.LL_API import LL_API
from ui.OrganizerUI import OrganizerUI
from ui.CaptainUI import CaptainUI
from ui.ShowGamesUI import ShowGamesUI
from ui.ViewerUI import ViewerUI
from ui.UI import Menu_functions
import os


class Main_Menu_UI:

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def header(self):
        """Displays a header artwork."""
        os.system('cls||clear')
        print(
            " _______________________________________________________________________________ \n"
            "|                                      ____                                     |\n"
            "|                                    /\ _ /\                                    |\n"
            "|                >>>----            / /\ /\ \                                   |\n"
            "|              >>>----             |---(*)---|                                  |\n"
            "|                                   \ \/_\/ /                                   |\n"
            "|                        >>>----     \/___\/                                    |\n"
            "|                                                                               |\n"
            "|                                                                               |\n"
            "|         █▀█ █ █  █▄▄ ▄▀█ █▀ █▀▀ █▀▄▀█ █▀▀ █▄ █ ▀█▀  █▀█ █▀█ █▀▀ █▄ █          |\n"
            "|         █▀▄ █▄█  █▄█ █▀█ ▄█ ██▄ █ ▀ █ ██▄ █ ▀█  █   █▄█ █▀▀ ██▄ █ ▀█          |\n"
            "| ______________________________________________________________________________|\n"
        )

    def displayMainMenu(self):
        "Displays Main menu screen."
        os.system('cls||clear')
        while True:
            self.header()
            print(

                "                                                                              \n"
                "                                                      ┈┈┏━╮╭━┓┈┈┈┈┈┈┈┈        \n"
                "   Aðalvalmynd                                        ┈┈┃┏┗┛┓┃┈┈┈┈┈┈┈┈        \n"
                "                                                      ┈┈╰┓▋▋┏╯┈┈┈┈┈┈┈┈        \n"
                "  1.  Mótshaldari                                     ┈╭━┻╮╲┗━━━━━╮╭╮┈        \n"
                "  2.  Fyrirliði                                       ┈┃▎▎┃╲╲╲╲╲╲╲┣━╯┈        \n"
                "  3.  Birta lista yfir viðureignir                    ┈╰━┳┻▅╯╲╲╲╲╲┃┈┈┈        \n"
                "  4.  Aðrir upplýsingar/ Tölfræði                     ┈┈┈╰━┳┓┏━┳┓┏╯┈┈┈        \n"
                "  q.  Hætta                                           ┈┈┈┈┈┗┻┛┈┗┻┛┈┈┈┈        \n"
                "                                                                              \n"
                "                                                        v. 0.0.1              \n"
                "\n")

            user_input = input("Veldu einn af valmöguleikunum hér að ofan: ")
            user_input = user_input.lower()
            if user_input == "q":
                os.system('cls||clear')
                Menu_functions.menuQuit()
            elif user_input == "1":
                OrganizerUI(self.llapi).displayOrganizerMenu()
            elif user_input == "2":
                os.system('cls||clear')
                CaptainUI(self.llapi).displayCaptainUI()
            elif user_input == "3":
                os.system('cls||clear')
                ShowGamesUI(self.llapi).showGamesPage()
            elif user_input == "4":
                os.system('cls||clear')
                ViewerUI(self.llapi).displayViewerUI()
            else:
                print()
                print("⛔ Ekki gildur valmöguleiki! Reynið aftur.")

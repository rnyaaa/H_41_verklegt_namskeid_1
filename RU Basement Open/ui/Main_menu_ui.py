from logic.LL_API import LL_API
from ui.OrganizerUI import OrganizerUI
from ui.CaptainUI import CaptainUI
from ui.ShowGamesUI import ShowGamesUI
from ui.ViewerUI import ViewerUI
from ui.UI import Menu_functions
import time


class Main_Menu_UI:

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayMainMenu(self):
        "Displays Main menu screen."
        while True:
            print(
                "\n"
                "                                      ____                                     \n"
                "                                    /\ _ /\                                    \n"
                "                >>>----            / /\ /\ \                                   \n"
                "              >>>----             ｜---(*)--｜                                 \n"
                "                                   \ \/_\/ /                                   \n"
                "                        >>>----     \/___\/                                    \n"
                "                                                                               \n"
                "                                                                               \n"
                "         █▀█ █ █  █▄▄ ▄▀█ █▀ █▀▀ █▀▄▀█ █▀▀ █▄ █ ▀█▀  █▀█ █▀█ █▀▀ █▄ █          \n"
                "         █▀▄ █▄█  █▄█ █▀█ ▄█ ██▄ █ ▀ █ ██▄ █ ▀█  █   █▄█ █▀▀ ██▄ █ ▀█          \n"
                " _______________________________________________________________________________\n"
                "｜                                                                              ｜\n"
                "｜                                                      ┈┈┏━╮╭━┓┈┈┈┈┈┈┈┈        ｜\n"
                "｜   Aðalvalmynd                                        ┈┈┃┏┗┛┓┃┈┈┈┈┈┈┈┈        ｜\n"
                "｜                                                      ┈┈╰┓▋▋┏╯┈┈┈┈┈┈┈┈        ｜\n"
                "｜  1.  Mótshaldari                                     ┈╭━┻╮╲┗━━━━━╮╭╮┈        ｜\n"
                "｜  2.  Fyrirliði                                       ┈┃▎▎┃╲╲╲╲╲╲╲┣━╯┈        ｜\n"
                "｜  3.  Birta lista yfir viðureignir                    ┈╰━┳┻▅╯╲╲╲╲╲┃┈┈┈        ｜\n"
                "｜  4.  Skoða Tölfræði                                  ┈┈┈╰━┳┓┏━┳┓┏╯┈┈┈        ｜\n"
                "｜  q.  Hætta                                           ┈┈┈┈┈┗┻┛┈┗┻┛┈┈┈┈        ｜\n"
                "｜                                                                              ｜\n"
                "｜                                                        v. 0.0.1              ｜\n"
                "｜______________________________________________________________________________｜\n"
                "\n")

            user_input = input("Veldu einn af valmöguleikunum hér að ofan: ")
            user_input = user_input.lower()

            if user_input == "q":
                Menu_functions.menuQuit()
            elif user_input == "1":
                OrganizerUI(self.llapi).displayOrganizerMenu()
            elif user_input == "2":
                CaptainUI(self.llapi).displayCaptainUI()
            elif user_input == "3":
                ShowGamesUI(self.llapi).showGamesPage()
            elif user_input == "4":
                ViewerUI(self.llapi).displayViewerUI()
            else:
                print()
                print("⛔ Ekki gildur valmöguleiki! Reynið aftur.")

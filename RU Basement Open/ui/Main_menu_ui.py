from logic.LL_API import LL_API
from ui.OrganizerUI import OrganizerUI
from ui.CaptainUI import CaptainUI
from ui.ShowGamesUI import ShowGamesUI
from ui.ViewerUI import ViewerUI


class Main_Menu_UI:

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayMainMenu(self):
        "Displays Main menu screen."
        while True:
            print(
                " ______________________________________________________________________________ \n"
                "|                                     ____                                     |\n"
                "|                                   /\ _ /\                                    |\n"
                "|               >>>----            / /\ /\ \                                   |\n"
                "|             >>>----             |---(*)---|                                  |\n"
                "|                                  \ \/_\/ /                                   |\n"
                "|                       >>>----     \/___\/                                    |\n"
                "|                                                                              |\n"
                "|                                                                              |\n"
                "|        █▀█ █ █  █▄▄ ▄▀█ █▀ █▀▀ █▀▄▀█ █▀▀ █▄ █ ▀█▀  █▀█ █▀█ █▀▀ █▄ █          |\n"
                "|        █▀▄ █▄█  █▄█ █▀█ ▄█ ██▄ █ ▀ █ ██▄ █ ▀█  █   █▄█ █▀▀ ██▄ █ ▀█          |\n"
                "|                                                                              |\n"
                "|______________________________________________________________________________|\n"
                "|                                                                              |\n"
                "|                                                      ┈┈┏━╮╭━┓┈┈┈┈┈┈┈┈        |\n"
                "|   Aðalvalmynd                                        ┈┈┃┏┗┛┓┃┈┈┈┈┈┈┈┈        |\n"
                "|                                                      ┈┈╰┓▋▋┏╯┈┈┈┈┈┈┈┈        |\n"
                "|  1.  Mótshaldari                                     ┈╭━┻╮╲┗━━━━━╮╭╮┈        |\n"
                "|  2.  Fyrirliði                                       ┈┃▎▎┃╲╲╲╲╲╲╲┣━╯┈        |\n"
                "|  3.  Birta lista yfir viðureignir                    ┈╰━┳┻▅╯╲╲╲╲╲┃┈┈┈        |\n"
                "|  4.  Aðrir notendur / Skoða Tölfræði                 ┈┈┈╰━┳┓┏━┳┓┏╯┈┈┈        |\n"
                "|  q.  Hætta                                           ┈┈┈┈┈┗┻┛┈┗┻┛┈┈┈┈        |\n"
                "|                                                                              |\n"
                "|                                                        v. 0.0.1              |\n"
                "|______________________________________________________________________________|\n"
                "\n")

            user_input = input("Veldu einn af valmöguleikunum hér að ofan: ")
            user_input = user_input.lower()

            if user_input == "q":
                print()
                print("     .--'''''''''--.")
                print("  .'      .---.      '.")
                print(" /    .-----------.    \ ")
                print("/        .-----.        \ ")
                print("|       .-.   .-.       |")
                print("|      /   \ /   \      |")
                print(" \    | .-. | .-. |    /")
                print("  '-._| | | | | | |_.-'")
                print("      | '-' | '-' |")
                print("       \___/ \___/")
                print("    _.-'  /   \  `-._")
                print("  .' _.--|     |--._ '.")
                print("  ' _...-|     |-..._ '")
                print("         |     |")
                print("         '.___.'")
                print()
                print("          Bless!")
                break
            elif user_input == "1":
                OrganizerUI(self.llapi).displayOrganizerMenu()
            elif user_input == "2":
                CaptainUI(self.llapi).displayCaptainUI()
            elif user_input == "3":
                ShowGamesUI(self.llapi).showGamesPage()
            elif user_input == "4":
                ViewerUI(self.llapi).displayViewerUI()
            else:
                print("Ekki gildur valmöguleiki!")



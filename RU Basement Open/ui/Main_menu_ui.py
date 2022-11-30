
from OrganizerUI import OrganizerUI
from CaptainUI import CaptainUI
from ShowGamesUI import ShowGamesUI
from ViewerUI import ViewerUI


class Main_Menu_UI():

    def __init__(self) -> None:
        pass
    
    def displayMainMenu():
        "Displays Main menu screen."
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
            "|                                                  |                           |\n"
            "|                                                  |   ┈┈┏━╮╭━┓┈┈┈┈┈┈┈┈        |\n"
            "|   Aðalvalmynd                                    |   ┈┈┃┏┗┛┓┃┈┈┈┈┈┈┈┈        |\n"
            "|                                                  |   ┈┈╰┓▋▋┏╯┈┈┈┈┈┈┈┈        |\n"
            "|  1.  Mótshaldari                                 |   ┈╭━┻╮╲┗━━━━━╮╭╮┈        |\n"
            "|  2.  Fyrirliði                                   |   ┈┃▎▎┃╲╲╲╲╲╲╲┣━╯┈        |\n"
            "|  3.  Birta lista yfir viðureignir                |   ┈╰━┳┻▅╯╲╲╲╲╲┃┈┈┈        |\n"
            "|  4.  Aðrir notendur / Skoða Tölfræði             |   ┈┈┈╰━┳┓┏━┳┓┏╯┈┈┈        |\n"
            "|  q.  Hætta                                       |   ┈┈┈┈┈┗┻┛┈┗┻┛┈┈┈┈        |\n"
            "|                                                  |                           |\n"
            "|                                                  |     v. 0.0.1              |\n"
            "|__________________________________________________|___________________________|\n"
            "\n")

    def input_prompt():
        while True:
            user_input = input("Veldu einn af valmöguleikunum hér að ofan: ")
            user_input = user_input.lower()
            
            if user_input == "q":
                break
            elif user_input == "1":
                menu = OrganizerUI()
                menu.displayOrganizerMenu()
            elif user_input == "2":
                menu = CaptainUI()
                menu.displayCaptainUI()
            elif user_input == "3":
                menu = ShowGamesUI()
                menu.showGamesPage()
            elif user_input == "4":
                menu = ViewerUI
                menu.displayViewerUI()
            else:
                print("Ekki gildur valmöguleiki!")

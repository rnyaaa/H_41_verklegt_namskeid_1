from logic.LL_API import LL_API
import time
import re


class Menu_functions:

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def menuFooter(display_quit=False):
        """Prints the last two options of a menu selection.

        If False: Only displays back option (ex. "b. Til baka")   <- False is the default
        If True: Also displays quit option (ex. "q. Quit")

        Finally asks the user for their selection and returns it."""

        print()
        print("b.	Til baka")
        if display_quit is True:
            print("q.	Hætta")

        print()
        user_input = input("Veldu einn af valmöguleikunum hér að ofan: ")
        user_input = user_input.lower()
        return user_input

    def menuExitCountdown(sec, dots_instead_of_sec=False):
        """Delays the execution of the functions that follow and displays a countdown.
        Takes in number of seconds and an optional bool (dots_instead_of_sec), false by default.

        If dots_instead_of_sec is True, dots will be displayed instead of a countdown in seconds."""
        countdown = sec
        time.sleep(1)
        print()
        print("Fer til baka í aðalvalmynd:")
        while countdown > 0:
            time.sleep(1)
            if dots_instead_of_sec is False:
                print(countdown)
            else:
                print(".")
            countdown -= 1
        print()

    def menuQuit():
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
        print("          Bless!\n")
        quit()

    def getPhoneNumber(ui_str: str):
        """Asks for, validates and returns phone number."""
        is_valid = False
        while not is_valid:
            try:
                phone_number = input(ui_str)
                is_valid = len(phone_number) == 7
                phone_number = int(phone_number)
            except ValueError:
                print("\nSímanúmer má aðeins innihalda 7 tölustafi. Reynið aftur.\n")
        return phone_number

    def getSSN(ui_str):
        """Asks for, validates and returns an Icelandid Social Security Number / SSN (kennitala)."""
        is_valid = False
        while not is_valid:
            try:
                ssn = input(ui_str).strip("-")
                is_valid = len(ssn) == 10
                ssn = int(ssn)
            except ValueError:
                print("\nKennitala má aðeins innihalda 10 tölustafi. Reynið aftur.\n")
        return ssn

    def getEmail(ui_str):
        """Asks for , validates and returns email address"""
        email_parameters = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        is_valid = False
        while not is_valid:
            email = input(ui_str)
            is_valid = re.fullmatch(email_parameters, email)
            if is_valid:
                return email
            print("\nÓgilt netfang, reynið aftur.\n")
            

# Viewer UI --------------------------------------------

class PlayerViewer():

    def enterPlayerName():

        None

    def showPlayer():
        None

    def showPlayerScoreByDate():
        None


class TournamentInfoUI():

    def displayTournamentInfo():
        print(">	Birta stöðu móts")
        print()
        # print( 1. KR	   |  9 stig  |  9 leggir unnir
        #   2. Valur   |  9 stig  |  8 leggir unnir
        #   3. Þróttur |  7 stig  |  5 leggir unnir
        print()

        user_input = Menu_functions.menuFooter(False)

        return user_input

    def showTournamentScores():
        None

    def showGamesFinished():
        None

    def showUpcomingGames():
        None

# ----------------------------------------------------------------------------------------------------


class PlayerHighScoreViewer():

    def showPlayerHighscore():
        """Prints a sorted list of players that have earned the most points in an orderly manner of  """
        """  List is as following
          print(➢ Þeir sem hafa [blank] (Top 10) _______________________________
#	|								|
#	|	1. 🥇	{Player_name}					|
#	|								|
#	|	2. 🥈	{Player_name}					|
#	|								|
#	|	3. 🥉	{Player_name}					|
#	|								|
#	|		4. 	{Player_name}				|
#	|		5. 	{Player_name}				|
#	|		6. 	{Player_name}				|
#	|		7.	{Player_name}				|
#	|		8.	{Player_name}				|
#	|		9.	{Player_name}				|
#	|		10. {Player_name}				|
#	|_______________________________________________________________|"""

        print(">	Listi yfir þá sem hafa skorað flest afreksstig.")
        print()
#      print(➢ Þeir sem hafa [blank] (Top 10) _______________________________
#	|								|
#	|	1. 🥇	{Player_name}					|
#	|								|
#	|	2. 🥈	{Player_name}					|
#	|								|
#	|	3. 🥉	{Player_name}					|
#	|								|
#	|		4. 	{Player_name}				|
#	|		5. 	{Player_name}				|
#	|		6. 	{Player_name}				|
#	|		7.	{Player_name}				|
#	|		8.	{Player_name}				|
#	|		9.	{Player_name}				|
#	|		10. {Player_name}				|
#	|_______________________________________________________________|

        print()

        user_input = Menu_functions.menuFooter(False)
        return user_input

    def sortPlayerHighscore():
        None


# Captain UI ----------------------------------------------------------------------

class CaptainUI():
    def displayCaptainUI():

        print(78*"_")
        print("                      ___     \n"
              "                    /\ _ /\   \n"
              "    >>>----        / /\ /\ \  \n"
              ">>>----           |---(*)---| \n"
              "                   \ \/_\/ /  \n"
              "        >>>----     \/___\/   \n"
              "\n")
        print(
            "Velkominn, Fyrirliði.\n"
            "\n\n"
            "➢  Valmynd:\n"
            "\n"
            "1.  Skrá úrslit viðureignar")
        user_input = Menu_functions.menuFooter(True)
        return user_input

    def openResultsMenu():
        None

# ----------------------------------------------------------------------------------------------------


class EnterResults():
    def showUpcomingGamesSel():
        None

    def openResultsForm():
        print()
        print("Veldu viðureign:\n")

        user_input = Menu_functions.menuFooter(True)
        return user_input

# ----------------------------------------------------------------------------------------------------


class ResultsForm():
    def AddResults():
        None

    def updatePlayers():
        None

    def updateTeams():
        None

    def updateGames():
        None

    def updateTournaments():
        None

    def updateResults():
        None

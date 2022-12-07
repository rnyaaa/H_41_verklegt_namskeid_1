from logic.LL_API import LL_API
import time
import re
import datetime


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

    def getPhoneNumber(ui_str: str):
        """Asks for, validates and returns phone number.
        Takes in the parameter ui_str, which is the string displayed for the input."""
        is_valid = False
        while not is_valid:
            try:
                phone_number = input(ui_str)
                is_valid = len(phone_number) == 7
                phone_number = int(phone_number)
                if not is_valid:
                    print(
                        "\n⛔ Símanúmer má aðeins innihalda 7 tölustafi. Reynið aftur.\n")
            except ValueError:
                print("\n⛔ Símanúmer má aðeins innihalda 7 tölustafi. Reynið aftur.\n")
        return phone_number

    def getSSN(ui_str: str):
        """Asks for, validates and returns an Icelandid Social Security Number / SSN (kennitala).
        Takes in the parameter ui_str, which is the string displayed for the input."""
        is_valid = False
        while not is_valid:
            try:
                ssn = input(ui_str).strip("-")
                is_valid = len(ssn) == 10
                ssn = int(ssn)
                if not is_valid:
                    print(
                        "\n⛔ Kennitala má aðeins innihalda 10 tölustafi. Reynið aftur.\n")
            except ValueError:
                print("\n⛔ Kennitala má aðeins innihalda 10 tölustafi. Reynið aftur.\n")
        return ssn

    def getEmail(ui_str: str):
        """Asks for , validates and returns email address.
        Takes in the parameter ui_str, which is the string displayed for the input."""
        email_parameters = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        is_valid = False
        while not is_valid:
            email = input(ui_str)
            is_valid = re.fullmatch(email_parameters, email)
            if is_valid:
                return email
            print("\n⛔ Ógilt netfang, reynið aftur.\n")

    def getDate(ui_str: str):
        """Asks for , validates and returns date information on the following format: dd.mm.yy
        Takes in the parameter ui_str, which is the string displayed for the input."""
        is_valid = False
        while not is_valid:
            date_str = input(ui_str)
            try:
                formatted_date = datetime.datetime.strptime(
                    date_str, '%d.%m.%y')
                is_valid = True
            except:
                print(
                    "\n⛔ Ógild dagsetning. Slá skal inn dagsetningu á forminu dd.mm.áá (t.d. 19.07.99)")
        return date_str

    def isBetweenDates(check_date, start, end):
        date = datetime.datetime.strptime(check_date, '%d.%m.%y')
        is_valid = False
        while not is_valid:
            start_date = datetime.datetime.strptime(start, '%d.%m.%y')
            end_date = datetime.datetime.strptime(end, '%d.%m.%y')

            if start_date <= date <= end_date:
                return check_date
            else:
                print(
                    f"⛔ Dagsetning er ekki í boði. Veldu dagsetningu á milli {start} og {end}.")

    def getEventDates():
        """Asks user for and returns start dates and end dates for an event on the format dd.mm.yy"""
        start_date = Menu_functions.getDate(
            "o	Byrjunardagsetning (dd.mm.yy): ")

        print(
            f"\no	Nær viðburðurinn yfir meira en einn dag ({start_date})?\n")
        print("y. Já" + "\n" + "n. nei\n")

        is_valid = False
        while not is_valid:
            is_multiple_days = input("Sláðu inn val þitt: ")
            if is_multiple_days.lower() == "n":
                end_date = start_date
                return start_date, end_date
            elif is_multiple_days.lower() == "y":
                end_date = Menu_functions.getDate(
                    "o	Lokadagsetning (dd.mm.yy): ")
                return start_date, end_date
            else:
                print("\n⛔ Ógilt val, reyndu aftur.\n")

    def getYesNo(ui_str: str):
        """Asks user yes or no. Takes in a custom string prompt (ui_str).
        Returns True for yes or False for no."""
        print(ui_str)
        print("\ny. Já" + "\n" + "n. nei\n")

        while True:
            user_choice = input("Sláðu inn val þitt: ")
            if user_choice.lower() == "n":
                return False
            if user_choice.lower() == "y":
                return True
            print("\n⛔ Ógilt val, reyndu aftur.\n")

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


# ----------------------------------------------------------------------------------------------------


class PlayerHighScoreViewer():

    def showPlayerHighscore():
        """Prints a sorted list of players that have earned the most points in an orderly manner."""

        """print(➢ Þeir sem hafa [blank] (Top 10) _______________________________
	|							                                	|
	|	1. 🥇	{Player_name}	                    				|
	|							                                	|
	|	2. 🥈	{Player_name}	                    				|
	|							                                	|
	|	3. 🥉	{Player_name}	                    				|
	|								                                |
	|		4. 	{Player_name}			                        	|
	|		5. 	{Player_name}			                        	|
	|		6. 	{Player_name}			                        	|
	|		7.	{Player_name}			                        	|
	|		8.	{Player_name}			                        	|
	|		9.	{Player_name}			                           	|
	|		10. {Player_name}				                        |
	|_______________________________________________________________|"""

        print(">	Listi yfir þá sem hafa skorað flest afreksstig.")
        print()

    def sortPlayerHighscore():
        None


# ----------------------------------------------------------------------------------------------------

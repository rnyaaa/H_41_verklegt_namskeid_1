from logic.LL_API import LL_API


class Menu_prompt:

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

        user_input = Menu_prompt.menuFooter(False)

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

        user_input = Menu_prompt.menuFooter(False)
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
        user_input = Menu_prompt.menuFooter(True)
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

        user_input = Menu_prompt.menuFooter(True)
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

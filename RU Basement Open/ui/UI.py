
from logic.LL_API import LL_API


class Main_Menu():

    def __init__(self) -> None:
        pass

    def displayMainMenu(self):
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
        
        user_input = input("Veldu einn af valmöguleikunum hér að ofan: ")

        #ekki viss hvort þetta ætti að vera hér? Ef ekki, hvar þá?        
        if user_input.lower() == "q":
            quit()
        
        return user_input
        
    def openOrganizerMenu(self):
        OrganizerUI.displayOrganizerMenu()

    def openViewerMenu(self):
        ViewerUI.displayViewer()

    def openCaptainMenu(self):
       CaptainUI.displayCaptainUI()

    def openShowGamesMenu(self):
        print(
        "Valmynd:\n"
        "\n"
        "1.	Listi yfir komandi viðureignir\n"
        "2.	Listi yfir yfirstaðnar viðureignir\n"
        "b.	Til baka\n")
        print()
        
        user_input = input("Veldu einn af valmöguleikunum hér að ofan: ")
        return user_input

    def language(self):
        # C-Requirement functionality to be implemented
        raise NotImplementedError

# Organizer UI --------------------------------------------

class OrganizerUI():

    def displayOrganizerMenu(self):
        print( 
        "   *** Velkominn, mótshaldari! ***\n"
        "\n"
        "Valmynd:\n"
        "\n"
        "1.	Skrá lið\n"
        "2.	Stofna deild\n"
        "3.	Skrá leikmenn\n"
        "4.	Breyta dagsetningu á viðureign\n"
        "5.	Breyta skráningu úrslita\n"
        "b. Til baka\n"
        "\n"
        )
        user_input = input("Veldu einn af valmöguleikunum hér að ofan: ")
        return user_input
        

    def addPlayer(self):
        print("➢   Skrá leikmenn")
        name = input("o Nafn: ")
        id_number = input("o    Kennitala: ")
        home_address = input("o Heimilisfang: ")
        phone_number1 = input("o GSM: ")
        phone_number2 = input("o    Heimasími: ")
        #email = input("o    Netfang: ")
        registered_team = input(
            f"Liðið sem leikmaðurinn tilheyrir:\n"
            # Hér kemur listi af liðum sem hafa verið skráð/á eftir að útfæra
        )
        LL_API.addPlayer(name, id_number, home_address, phone_number1, phone_number2, registered_team)
        
        
    def addTeamPage(self):
        print("➢   Skrá lið:")
        print()
        team_name = input("o   Nafn liðs: ")
        home_address = input("o   Heimilisfang: ")
        phone_number = input("o   Símanúmer: ")
        
        return team_name, home_address, phone_number

    def addTournament(self):
        print("➢	Stofna deild:")
        print()
        tournament_name = input("o     Nafn deildar: ")
        organizer_name = input("o    Nafn Skipuleggjanda: ")
        organizer_number = input("o     Símanúmer skipuleggjanda: ")
        tournament_type = input("o     Tegund móts: ")
        while True:
            dates = input("o    Dagsetningar: ")
            if dates == "":
                break

        return tournament_name, organizer_name, organizer_number, tournament_type, dates


    def changeTournamentDates(self):
        print("➢	Breyta dagsetningu á viðureign: \n")
        print()
        print("     Veldu viðureign\n")
        print()
        #print(hér koma viðureignirnar)
        print()
        back = input("b. Til baka")
        quits = input("q. Hætta")

        return back, quits
        

    def changeResults(self):
        print("➢	Breyta skráningu úrslita:\n ")
        print()
        print("     Veldu úrslit: ")
        print()
        #print(hér kemur tafla með úrslitum )
        print()
        back = input("b. Til baka")
        quits = input("q. Hætta")

        return back, quits


class ChangeTournamentDatesUI():

    def showUpcomingGamesSel(self):
        pass

    def openTournamentForm(self):
        pass

class ChangeTournamentFormUI():

    def changeTournament(self):
        pass

    def updateGames(self):
        pass

    def updateTournaments(self):
        pass
    

class AddTournamentPageUI():

    def showUpcomingGames(self):
        pass

    def openTournamentForm(self):
        pass

class AddtournamentFormUI():

    def addTournament(self):
        pass

    def upadateGames(self):
        pass

    def updateTournaments(self):
        pass


class ChangeResultsPageUI():

    def showGamesFinishedSel(self):
        pass

    def openResultsForm(self):
        pass

class ChangeResultsFormUI():

    def changeResults(self):
        pass

    def updatePlayers(self):
        pass

    def updateTeams(self):
        pass

    def updateGames(self):
        pass

    def updateTournaments(self):
        pass

    def updateResults(self):
        pass

class AddteamPageUI():

    def showTeams(self):
        pass
    
    def openTeamsForm(self):
        pass

class AddteamFormUI():
    
    def addTeam(self):
        pass

    def updatePlayers(self):
        pass

    def updateTeams(self):
        pass

class AddPlayerUI():

    def showTeams(self):
        pass

    def openPlayerForm(self):
        pass

class AddPlayerFormUI():
    
    def addPlayer(self):
        pass

    def updatePlayers(self):
        pass

    def updateTeams(self):
        pass


class ShowGamesUI():

    def showGamesPage(self):
        raise NotImplementedError

    def showTournamentDates(self):
        raise NotImplementedError

    def showGamesFinished(self):
        raise NotImplementedError

    def showUpcomingGames(self):
        raise NotImplementedError


# Viewer UI --------------------------------------------

class ViewerUI:

    def displayViewer(self):
        print(input(
        "*** Verið velkomin í Tölfræðivalmyndina! ***\n"
        "\n"
        "➢ Valmynd:\n"
        "\n"
        "1.	Listi yfir liðum\n"
        "2.	Staða móts\n"
        "3. Listi yfir þá sem hafa skorað flest afreksstig\n"
        "4.	Listi yfir þá sem eiga besta/hæsta innskotið á mótinu/deildinni\n"
        "5.	Listi yfir þá sem eiga besta/hæsta útskotið á mótinu/deildinni\n"
        "6.	Tölfræði fyrir ákveðna leikmenn\n"
        "b.	Til baka\n"
        "\n"
        ))
        selection = print(input("Veldu einn af valmöguleikunum hér að ofan: "))
        return selection
        
    def showTournamentInfo(self):
        None

    def showTeamViewer(self):
        None

    def showPlayerViewer(self):
        None

    def showPlayerHighscoreViewer(self):
        None


class TeamViewer():

    def showTeams(self):
        print(">	Birta lista yfir Liðum\n")
        print()
        #print("lið"
        #       Nafn
        #       Nafn
        #       Nafn
        #  "lið"  
        #       Nafn   )
        
        print()
        
        user_input = input("b. til baka")
        
        if user_input.lower() == "b":
            return


class PlayerViewer():

    def enterPlayerName(self):
        None

    def showPlayer(self):
        None

    def showPlayerScoreByDate(self):
        None


class TournamentInfoUI():

    def displayTournamentInfo(self):
        print(">	Birta stöðu móts")
        print()
        #print( 1. KR	   |  9 stig  |  9 leggir unnir
	        #   2. Valur   |  9 stig  |  8 leggir unnir
	        #   3. Þróttur |  7 stig  |  5 leggir unnir
        print()
        
        user_input = input("b. til baka")
        
        if user_input.lower() == "b":
            return


    def showTournamentScores(self):
        None

    def showGamesFinished(self):
        None

    def showUpcomingGames(self):
        None


class PlayerHighScoreViewer():

    def showPlayerHighscore(self):
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
        
        user_input = input("b. til baka")
        
        if user_input.lower() == "b":
            return
        
    def sortPlayerHighscore(self):
        None


# Captain UI --------------------------------------------

class CaptainUI():
    def displayCaptainUI(self):

        print(input(
        "                      ___     \n"
        "                    /\ _ /\   \n"
        "    >>>----        / /\ /\ \  \n"
        ">>>----           |---(*)---| \n"
        "                   \ \/_\/ /  \n"
        "        >>>----     \/___\/   \n"
        "\n"    
        "     *** Halló, Fyrirliði! ***\n"
        "\n"
        "1.  Skrá úrslit viðureignar\n"
        "b.  Til baka\n"
        "q.  Hætta\n"
        "\n"
        "Veldu einn af valmöguleikunum hér að ofan: "
        ))

    def openResultsMenu(self):
        None
    
class EnterResults():
    def showUpcomingGamesSel(self):
        None

    def openResultsForm(self):
        input(
        "Veldu viðureign\n"
  
        "b. Til baka\n"
        "q. Hætta\n" 
        )
        

class ResultsForm():
    def AddResults(self):
        None
    
    def updatePlayers(self):
        None
    
    def updateTeams(self):
        None
    
    def updateGames(self):
        None
    
    def updateTournaments(self):
        None
    
    def updateResults(self):
        None

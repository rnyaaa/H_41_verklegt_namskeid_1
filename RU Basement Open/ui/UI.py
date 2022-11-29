from logic.LL_API import LL_API


class Main_Menu():
    def displayMainMenu():
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
        
        return user_input
        
    def openOrganizerMenu():
        OrganizerUI.displayOrganizerMenu()

    def openViewerMenu():
        ViewerUI.displayViewer()

    def openCaptainMenu():
       CaptainUI.displayCaptainUI()

    def openShowGamesMenu():
        print(
        "Valmynd:\n"
        "\n"
        "1.	Listi yfir komandi viðureignir\n"
        "2.	Listi yfir yfirstaðnar viðureignir\n"
        "b.	Til baka\n")
        print()
        
        user_input = input("Veldu einn af valmöguleikunum hér að ofan: ")
        return user_input


    def language():
        # C-Requirement functionality to be implemented
        raise NotImplementedError

    def backQuitMenu(display_quit):
        """Prints the last two options of a menu selection (b for Back and q for Quit).
        Also asks user for their selection and returns it."""

        print()
        print("b.	Til baka")
        if display_quit is True:
            print("q.	Hætta")

        print() 
        user_input = input("Veldu einn af valmöguleikunum hér að ofan: ")
        return user_input  
        

# Organizer UI --------------------------------------------

class OrganizerUI():

    def displayOrganizerMenu():
        print()
        print( 
        "   *** Velkominn, mótshaldari! ***\n"
        "\n"
        "Valmynd:\n"
        "\n"
        "1.	Skrá lið\n"
        "2.	Stofna deild\n"
        "3.	Skrá leikmenn\n"
        "4.	Breyta dagsetningu á viðureign\n"
        "5.	Breyta skráningu úrslita\n")
        
        user_input = Main_Menu.backQuitMenu(True)
        return user_input
        

    def addPlayer():
        print("➢   Skrá leikmenn")
        name = input("o Nafn: ")
        id_number = input("o    Kennitala: ")
        home_address = input("o     Heimilisfang: ")
        phone_number1 = input("o    GSM: ")
        phone_number2 = input("o    Heimasími: ")
        #email = input("o    Netfang: ")
        registered_team = input(
            f"Liðið sem leikmaðurinn tilheyrir:\n"
            # Hér kemur listi af liðum sem hafa verið skráð/á eftir að útfæra
        )
        LL_API.addPlayer(name, id_number, home_address, phone_number1, phone_number2, registered_team)
        
        
    def addTeamPage():
        print("➢   Skrá lið:")
        print()
        team_name = input("o   Nafn liðs: ")
        home_address = input("o   Heimilisfang: ")
        team_organiser = input("o   Nafn félags: ")
        phone_number = input("o   Símanúmer: ")
        
         # MUNA AÐ LAGA ÞETTA - INTEGRATE-A OG LÁTA LL API SJÁ UM
        LL_API.addTeam(team_name, home_address, team_organiser, phone_number)

    def addTournament():
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
        
        # Má gera lista að ofan til að geyma dagsetingar?
        # MUNA AÐ LAGA ÞETTA - INTEGRATE-A OG LÁTA LL API SJÁ UM
        LL_API.addTournament(tournament_name, organizer_name, organizer_number, tournament_type, dates)


    def changeTournamentDates():
        print("➢	Breyta dagsetningu á viðureign: \n")
        print()
        print("     Veldu viðureign\n")
        print()
        #print(hér koma viðureignirnar)
        print()

        user_input = Main_Menu.backQuitMenu(True)
        return user_input      

    def changeResults():
        print("➢	Breyta skráningu úrslita:\n ")
        print()
        print("	Veldu úrslit: ")
        print()

        #print(hér kemur tafla með úrslitum )
        
        user_input = Main_Menu.backQuitMenu(True)
        return user_input 


class ChangeTournamentDatesUI():

    def showUpcomingGamesSel():
        pass

    def openTournamentForm():
        pass

class ChangeTournamentFormUI():

    def changeTournament():
        pass

    def updateGames():
        pass

    def updateTournaments():
        pass
    

class AddTournamentPageUI():

    def showUpcomingGames():
        pass

    def openTournamentForm():
        pass

class AddtournamentFormUI():

    def addTournament():
        pass

    def upadateGames():
        pass

    def updateTournaments():
        pass


class ChangeResultsPageUI():

    def showGamesFinishedSel():
        pass

    def openResultsForm():
        pass

class ChangeResultsFormUI():

    def changeResults():
        pass

    def updatePlayers():
        pass

    def updateTeams():
        pass

    def updateGames():
        pass

    def updateTournaments():
        pass

    def updateResults():
        pass

class AddteamPageUI():

    def showTeams():
        pass
    
    def openTeamsForm():
        pass

class AddteamFormUI():
    
    def addTeam():
        pass

    def updatePlayers():
        pass

    def updateTeams():
        pass

class AddPlayerUI():

    def showTeams():
        pass

    def openPlayerForm():
        pass

class AddPlayerFormUI():
    
    def addPlayer():
        pass

    def updatePlayers():
        pass

    def updateTeams():
        pass


class ShowGamesUI():

    def showGamesPage():
        raise NotImplementedError

    def showTournamentDates():
        raise NotImplementedError

    def showGamesFinished():
        raise NotImplementedError

    def showUpcomingGames():
        raise NotImplementedError


# Viewer UI --------------------------------------------

class ViewerUI:

    def displayViewer():
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
        
    def showTournamentInfo():
        None

    def showTeamViewer():
        None

    def showPlayerViewer():
        None

    def showPlayerHighscoreViewer():
        None


class TeamViewer():

    def showTeams():
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
        #print( 1. KR	   |  9 stig  |  9 leggir unnir
	        #   2. Valur   |  9 stig  |  8 leggir unnir
	        #   3. Þróttur |  7 stig  |  5 leggir unnir
        print()
        
        user_input = input("b. til baka")
        
        if user_input.lower() == "b":
            return


    def showTournamentScores():
        None

    def showGamesFinished():
        None

    def showUpcomingGames():
        None


class PlayerHighScoreViewer():

    def showPlayerHighscore():
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
        
    def sortPlayerHighscore():
        None


# Captain UI --------------------------------------------

class CaptainUI():
    def displayCaptainUI():

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

    def openResultsMenu():
        None
    
class EnterResults():
    def showUpcomingGamesSel():
        None

    def openResultsForm():
        input(
        "Veldu viðureign\n"
  
        "b. Til baka\n"
        "q. Hætta\n" 
        )
        

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

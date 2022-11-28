
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
            )

    def openOrganizerMenu():
        print("Velkominn, mótshaldari."

                    "Valmynd:"

                "1.	Skrá lið"
                "2.	Stofna deild"
                "3.	Skrá leikmenn"
                "4.	Breyta dagsetningu á viðureign"
                "5.	Breyta skráningu úrslitaa"
                "b. 	Til baka"
            
                    "Veldu einn af valmöguleikunum hér að ofan: "
                ) 
    def openViewerMenu():
        raise NotImplementedError

    def openCaptainMenu():
        raise NotImplementedError

    def openShowGamesMenu():
        raise NotImplementedError

    def language():
        # C-Requirement functionality to be implemented
        raise NotImplementedError

# Organizer UI --------------------------------------------

class OrganizerUI():

    def displayOrganizerMenu():
        pass

    def addPlayer():
        pass

    def addTeamPage():
        pass

    def addTournament():
        pass

    def changeTournamentDates():
        pass

    def changeResults():
        pass


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

class viewerUI:

    def displayViewer():
        None

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
        None


class PlayerViewer():

    def enterPlayerName():
        None

    def showPlayer():
        None

    def showPlayerScoreByDate():
        None


class TournamentInfoUI():

    def displayTournamentInfo():
        None

    def showTournamentScores():
        None

    def showGamesFinished():
        None

    def showUpcomingGames():
        None


class PlayerHighScoreViewer():

    def showPlayerHighscore():
        None

    def sortPlayerHighscore():
        None


# Captain UI --------------------------------------------

class CaptainUI():
    def displayCaptainUI():
        None

    def openResultsMenu():
        None
    
class EnterResults():
    def showUpcomingGamesSel():
        None

    def openResultsForm():
        None
    

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

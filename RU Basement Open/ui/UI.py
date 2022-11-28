
class Main_Menu():

    def displayMainMenu():
        raise NotImplementedError

    def openOrganizerMenu():
        raise NotImplementedError

    def openViewerMenu():
        raise NotImplementedError

    def openCaptainMenu():
        raise NotImplementedError

    def openShowGamesMenu():
        raise NotImplementedError

    def language():
        # C-Requirement functionality to be implemented
        raise NotImplementedError


class ShowGamesUI():

    def showGamesPage():
        raise NotImplementedError

    def showTournamentDates():
        raise NotImplementedError

    def showGamesFinished():
        raise NotImplementedError

    def showUpcomingGames():
        raise NotImplementedError


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


# CAPTAIN UI --------------------------------------------

class CaptainUI
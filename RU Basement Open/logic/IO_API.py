class Viewer(): 
    
      
    def getPlayers(self):
        return PlayerLL.getPlayers()

    def getTeams():
        raise NotImplementedError

    def getTournaments():
        raise NotImplementedError

    def getGames():
        raise NotImplementedError

    def getPlayerList():
        raise NotImplementedError

    def getPlayerScore():
        raise NotImplementedError

    def getPlayerScoreByDate():
        raise NotImplementedError

    def getTournamentScores():
        raise NotImplementedError
    
    def getTournamentScores():
        raise NotImplementedError
    
    def getGamesFinished():
        raise NotImplementedError
    
    def getUpcomingGames():
        raise NotImplementedError


class PlayerListLL():
    def getPlayer():
        raise NotImplementedError
    
    def getPlayerSortQP():
        raise NotImplementedError
    
    def getPlayerSortInshorts():
        raise NotImplementedError
    
    def getPlayerSortOutshot():
        raise NotImplementedError
    

class PlayersLL():
    def getPlayers():
        return IO_API.getPlayers()
    
    def getResults():
        raise NotImplementedError
    
    def addPlayers():
        raise NotImplementedError
    
    def updatePlayers():
        raise NotImplementedError

    
class Tournament():
    def getTournament():
        raise NotImplementedError
    
    def getGames():
        raise NotImplementedError
    
    def getResults():
        raise NotImplementedError

    def updateTournament():
        raise NotImplementedError
    
    def updateGames():
        raise NotImplementedError

class Game():
    def getTournament():
        raise NotImplementedError
    
    def getGames():
        raise NotImplementedError

    def getResults():
        raise NotImplementedError
    
    def addGame():
        raise NotImplementedError

    def changeDate():
        raise NotImplementedError
    
    def updateGames():
        raise NotImplementedError

    def updateTournament():
        raise NotImplementedError
    

class Results():
    def getResults():
        raise NotImplementedError

    def changeResults():
        raise NotImplementedError

    def updateResults():
        raise NotImplementedError
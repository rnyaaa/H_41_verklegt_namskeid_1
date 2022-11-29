from LL_API import LL_API
class TournamentLL():

    def getTournament():
        tournamentstream = LL_API.getTournaments()
        return tournamentstream
        
    def getGames():
        gamestream = LL_API.getGames()
        return gamestream
    
    def getResults(resultsID):
        resultstream = LL_API.getResults(resultsID)
        return resultstream

    def addTournament():
        raise NotImplementedError

    def updateTournament():
        raise NotImplementedError
    
    def updateGames():
        raise NotImplementedError
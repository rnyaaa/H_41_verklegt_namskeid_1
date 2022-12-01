from IO.IO_API import IO_API

class GamesLL():

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def addGame():
        None

    def changeDate():
        None

    def getGameFinished(self):
        """ Gets finished games by checking whether results have been added. Adds games with results to list"""
        games = self.ioapi.getGames()
        gamesfinished = []
        for game in games:
            if games[game][4] != None:
                gamesfinished.append([games[game][0], games[game][1], games[game]
                                     [3], games[game][4], games[game][5], games[game][6]])
                """ Team 1, Team 2, Date, Winner, ScoreWinner, ScoreLoser"""
        return gamesfinished

    def getUpcomingGames(self):
        """ Gets upcoming games by checking whether results have been added. Adds games with no results to list"""
        games = self.ioapi.getGames()
        gamesupcoming = []
        for game in games:
            if games[game][4] == None:
                gamesupcoming.append(
                    [games[game][0], games[game][1], games[game][3]])
                """ Team 1, Team 2, Date"""
        return gamesupcoming
from IO.IO_API import IO_API

class ResultsLL:

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def changeResults(self, resultsID):
        raise NotImplementedError

    def updateResults(self, results, resultsID):
        raise NotImplementedError

    def updatePlayers(self, results):
        raise NotImplementedError

    def updateGames(self, results):
        raise NotImplementedError

    def updateTeams(self, results):
        raise NotImplementedError
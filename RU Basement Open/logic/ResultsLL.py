from IO.IO_API import IO_API
from models.results import Results
from models.player import Player
from models.team import Team
from models.playerscore import PlayerScore

class ResultsLL:

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def getAllResults(self):
        return self.ioapi.return_model(Results)

    def changeResults(self, results_id, newresults: Results):
        results_list = self.getAllResults()
        for instance in results_list:
            if instance.results_id == results_id:
                results_list.remove(instance)
                results_list.append(newresults)
        self.ioapi.overwrite_model(results_list)
    
    def addResults(self, results: Results):
        """ adds results """
        self.ioapi.create_model(results)
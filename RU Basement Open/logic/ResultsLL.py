from IO.IO_API import IO_API
from models.results import Results
from models.player import Player
from models.playerscore import PlayerScore

class ResultsLL:

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def getAllResults(self):
        return self.ioapi.return_model(Results)

    def changeResults(self, results_id):
        all_results = self.getAllResults()
        for result in all_results:
            if Results.results_id == results_id:
                return Results
    
    # player_intermediate = [playerid, QPs, inshots, outshots 501win, 501lose, 501fwin 501flose, 301win, 301lose, cricketwin, cricketlose]
    def addResults(self, results: Results):
        playersaward = [[Results.players[0]],[Results.players[1]],[Results.players[2]],[Results.players[3]],[Results.players[4]],[Results.players[5]],[Results.players[6]],[Results.players[7]]]
        for i in range(0, len(Results.QPs_awarded),2):
            for j in range(0, len(playersaward)):
                if Results.QPs_awarded[i] == playersaward[j][0]:
                    playersaward[j].append(Results.QPs_awarded[i+1])
                    

        
            
            

        

    def updatePlayers(self, results):
        raise NotImplementedError

    def updateGames(self, results):
        raise NotImplementedError

    def updateTeams(self, results):
        raise NotImplementedError
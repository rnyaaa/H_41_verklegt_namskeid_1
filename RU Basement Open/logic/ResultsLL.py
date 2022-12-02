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

    def changeResults(self, results_id):
        all_results = self.getAllResults()
        for result in all_results:
            if Results.results_id == results_id:
                return Results
    
    # player_intermediate = [playerid, QPs, inshots, outshots 501win, 501lose, 501fwin 501flose, 301win, 301lose, cricketwin, cricketlose]
    def addResults(self, results: Results):
        playersaward = [[Results.players[0]],[Results.players[1]],[Results.players[2]],[Results.players[3]],[Results.players[4]],[Results.players[5]],[Results.players[6]],[Results.players[7]]]
        """ QPs awarded by iterating through the playerid list and then matching to the playerid in results and appending the points to that"""
        for i in range(0, len(Results.QPs),2):
            for j in range(0, len(playersaward)):
                if Results.QPs[i] == playersaward[j][0]:
                    playersaward[j].append(Results.QPs[i+1])
        """ Inshots awarded """
        for i in range(0, len(Results.inshots),2):
            for j in range(0, len(playersaward)):
                if Results.inshots[i] == playersaward[j][0]:
                    playersaward[j].append(Results.inshots[i+1])
        """ Outshots awarded """
        for i in range(0, len(Results.outshots),2):
            for j in range(0, len(playersaward)):
                if Results.outshots[i] == playersaward[j][0]:
                    playersaward[j].append(Results.outshots[i+1])
        """ 501 wins awarded """
        for i in range(0, len(Results.winning501s)):
            for j in range(0, len(playersaward)):
                if Results.winning501s[i] == playersaward[j][0]:
                    playersaward[j].append(1)
        """ 501 lose awarded lol """
        for i in range(0, len(Results.losing501s)):
            for j in range(0, len(playersaward)):
                if Results.losing501s[i] == playersaward[j][0]:
                    playersaward[j].append(1)
        """ 301 wins awarded """
        for i in range(0, len(Results.winning301)):
            for j in range(0, len(playersaward)):
                if Results.winning301[i] == playersaward[j][0]:
                    playersaward[j].append(1)
        """ 301 lose awarded lol """
        for i in range(0, len(Results.losing301)):
            for j in range(0, len(playersaward)):
                if Results.losing301[i] == playersaward[j][0]:
                    playersaward[j].append(1)
        """ cricket wins awarded """
        for i in range(0, len(Results.winningcricket)):
            for j in range(0, len(playersaward)):
                if Results.winningcricket[i] == playersaward[j][0]:
                    playersaward[j].append(1)
        """ cricket lose awarded lol """
        for i in range(0, len(Results.losingcricket)):
            for j in range(0, len(playersaward)):
                if Results.losingcricket[i] == playersaward[j][0]:
                    playersaward[j].append(1)
        """ 501f wins awarded """
        for i in range(0, len(Results.winning501f)):
            for j in range(0, len(playersaward)):
                if Results.winning501f[i] == playersaward[j][0]:
                    playersaward[j].append(1)
        """ 501f lose awarded lol """
        for i in range(0, len(Results.losing501f)):
            for j in range(0, len(playersaward)):
                if Results.losing501f[i] == playersaward[j][0]:
                    playersaward[j].append(1)

        for item in playersaward:
            self.addPlayerScore(PlayerScore(Results.game_id, item[0], item[1], item[2], item[3], (item[4], item[5]), (item[6], item[7]), (item[8], item[9]), (item[10], item[11])))
        
        """ edit teamscores """
        teams = self.ioapi.return_model(Team)
        teamupdate = [[Results.winningscore[0]], [Results.losingscore[0]]]
        for i in range(0, len(teams)):
            if teams.id == Res:



    def addPlayerScore(self, playerscore: PlayerScore):
        """ adds a playerscore """
        self.ioapi.create_model(playerscore)                    

    def updatePlayers(self, results):
        raise NotImplementedError

    def updateGames(self, results):
        raise NotImplementedError

    def updateTeams(self, results):
        raise NotImplementedError
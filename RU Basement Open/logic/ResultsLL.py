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
        resultslist = []
        for instance in results_list:
            if instance.results_id == results_id:
                results_list.remove(instance)
                results_list.append(newresults)
        self.ioapi.overwrite_model(results_list)
    
    def IterateResults(self, results: Results, type, iterator_length, playersaward, isratio: bool):
        for i in range(0, len(results.type), iterator_length):
            for j in range(0, len(playersaward)):
                if results.type[i] == playersaward[j][0]:
                    if isratio:
                        playersaward[j].append(1)
                    else:
                        playersaward[j].append(results.type[i+1])
    # player_intermediate = [playerid, QPs, inshots, outshots 501win, 501lose, 501fwin 501flose, 301win, 301lose, cricketwin, cricketlose]
    def addResults(self, results: Results):
        playersaward = [[Results.players[0]],[Results.players[1]],[Results.players[2]],[Results.players[3]],[Results.players[4]],[Results.players[5]],[Results.players[6]],[Results.players[7]]]
        """ QPs awarded by iterating through the playerid list and then matching to the playerid in results and appending the points to that"""
        playersaward = self.IterateResults(Results, QPs, 2, playersaward, False)
        playersaward = self.IterateResults(Results, inshots, 2, playersaward, False)
        playersaward = self.IterateResults(Results, outshots, 2, playersaward, False)
        playersaward = self.IterateResults(Results, winning501s, 1, playersaward, True)
        playersaward = self.IterateResults(Results, losing501s, 1, playersaward, True)
        playersaward = self.IterateResults(Results, winning301, 1, playersaward, True)
        playersaward = self.IterateResults(Results, losing301, 1, playersaward, True)
        playersaward = self.IterateResults(Results, winningcricket, 1, playersaward, True)
        playersaward = self.IterateResults(Results, losingcricket, 1, playersaward, True)
        playersaward = self.IterateResults(Results, winning501f, 1, playersaward, True)
        playersaward = self.IterateResults(Results, losing501f, 1, playersaward, True)

        for item in playersaward:
            self.addPlayerScore(PlayerScore(Results.game_id, item[0], item[1], item[2], item[3], (item[4], item[5]), (item[6], item[7]), (item[8], item[9]), (item[10], item[11])))
        
        """ edit teamscores """
        teams = self.ioapi.return_model(Team)
        teamupdate = []
        for i in range(0, len(teams)):
            if teams[i].id == Results.winningscore[0]:
                teamupdate.append(Team(teams[i].id, teams[i].name, teams[i].address, teams[i].club_name, teams[i].phone, teams[i].games_won + Results.winningscore[1], teams[i].rounds_won + Results.winngingscore[2], teams[i].player1, teams[i].player2, teams[i].player3, teams[i].player4))
                teams.remove(teams[i])
            if teams[i].id == Results.losingscore[0]:
                teamupdate.append(Team(teams[i].id, teams[i].name, teams[i].address, teams[i].club_name, teams[i].phone, teams[i].games_won + Results.losingscore[1], teams[i].rounds_won + Results.losingscore[2], teams[i].player1, teams[i].player2, teams[i].player3, teams[i].player4))
                teams.remove(teams[i])
        teams.append(teamupdate[0], teamupdate[1])
        self.ioapi.overwrite_model(teams)


    def addPlayerScore(self, playerscore: PlayerScore):
        """ adds a playerscore """
        self.ioapi.create_model(playerscore)                    

    def updatePlayers(self, results):
        raise NotImplementedError

    def updateGames(self, results):
        raise NotImplementedError

    def updateTeams(self, results):
        raise NotImplementedError
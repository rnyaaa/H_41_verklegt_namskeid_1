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
    
    def IterateResults(self, resultlist, iterator_length, playersaward, isratio: bool):
        for i in range(0, len(resultlist), iterator_length):
            for j in range(0, len(playersaward)):
                if resultlist[i] == playersaward[j][0]:
                    if isratio:
                        playersaward[j].append(1)
                    else:
                        playersaward[j].append(resultlist[i+1])

    # player_intermediate = [playerid, QPs, inshots, outshots 501win, 501lose, 501fwin 501flose, 301win, 301lose, cricketwin, cricketlose]
    def addResults(self, results: Results):
        playersaward = [[results.players[0]],[results.players[1]],[results.players[2]],[results.players[3]],[results.players[4]],[results.players[5]],[results.players[6]],[results.players[7]]]
        """ QPs awarded by iterating through the playerid list and then matching to the playerid in results and appending the points to that"""
        playersaward = self.IterateResults(results.QPs_awarded, 2, playersaward, False)
        playersaward = self.IterateResults(results.inshots_awarded, 2, playersaward, False)
        playersaward = self.IterateResults(results.outshots_awarded, 2, playersaward, False)
        playersaward = self.IterateResults(results.winning501s, 1, playersaward, True)
        playersaward = self.IterateResults(results.losing501s, 1, playersaward, True)
        playersaward = self.IterateResults(results.winning301, 1, playersaward, True)
        playersaward = self.IterateResults(results.losing301, 1, playersaward, True)
        playersaward = self.IterateResults(results.winningcricket, 1, playersaward, True)
        playersaward = self.IterateResults(results.losingcricket, 1, playersaward, True)
        playersaward = self.IterateResults(results.winning501f, 1, playersaward, True)
        playersaward = self.IterateResults(results.losing501f, 1, playersaward, True)

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
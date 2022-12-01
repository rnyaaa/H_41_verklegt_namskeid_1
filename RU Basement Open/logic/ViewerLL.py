from IO.IO_API import IO_API
from models.player import Player
from models.playerscore import PlayerScore
from models.team import Team
from models.tournament import Tournament



# from logic.LL_API import LL_API

# verðum að hætta að importa LL_API inn í hina LL klasana, annars fáum við circular import
# Megum bara importa hinum LL klösunum inn í LL_API en ekki öfugt!


class ViewerLL:
    def __init__(self, ioapi_connection: IO_API):
        self.ioapi = ioapi_connection

    def sort(item):
        """ function to implement keysort for the playersort functions """
        return item[1]

    def getPlayerList(self, sortkey):
        """ Sorts the players according to QPs, Inshots or Outshots. 
            The attribute this functions gets called by should be either of those."""
        players = self.ioapi.getAll("players")
        playerscores = self.ioapi.getAll("playerscore")
        list = []
        if sortkey == QP:
            sortkey = 5
            # goes to the item in the list that tracks QPs
        if sortkey == inshots:
            sortkey = 6
        if sortkey == outshots:
            sortkey = 7
        for player in players:
            list.append([players[player], players[player][sortkey]])
            # gets a list like [[playername, QPs]]
        list.sort(key=sort)
        return list

    def getPlayerScore(self):
        """ Takes the playerstream, finds the player and takes the values from 8-19 and puts them in an array and returns it """
        players = self.ioapi.getPlayers()
        scores = []
        for player in players:
            if players[player][0] == playername:
                scores = [line[8], line[9], line[10], line[11], line[12], line[13],
                          line[14], line[15], line[16], line[17], line[18], line[19]]
                """ 501 Einmenn, unnir, tap, 301 Duo, unnir, tap, Cricket, unnir, tap,501 Fjormenn, unnir, tap"""
        return scores

    def getPlayerScoreByDate():
        raise NotImplementedError

    def getTournamentScore(self):
        teams = self.ioapi.getTeams()
        """ gets all teams in tournament and sorts by games won and rounds won """
        # NOTE: Implement the sorting so that it sorts by both, as it is it only sorts by games won
        tournamentranklist = []
        for team in teams:
            tournamentranklist.append([line[0], line[4], line[5]])
            # team_name, games won, rounds won
        tournamentranklist.sort()
        return tournamentranklist

    def getTournamentDates(self):
        """ sækir tournament skrá, fer í línu 2 með dagsetningum og liðum sem spila þann dag og setur í lista """
        tournamentdatelist = []
        tournaments = self.ioapi.getTournament()
        """ google svartagaldur, pls finna betri leið til að taka hvert 3 gildi og setja í list """
        tournamentdatelist = zip(*[iter(tournaments[1])]*3)
        return tournamentdatelist

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

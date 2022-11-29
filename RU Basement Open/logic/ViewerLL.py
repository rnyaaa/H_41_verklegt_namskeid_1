
from logic.LL_API import LL_API

class ViewerLL:
    def getPlayers():
        playerstream = LL_API.getPlayers()
        return playerstream
        
    def getTeams():
        teamstream = LL_API.getTeams()
        return teamstream

    def getGames():
        gamestream = LL_API.getGames()
        return gamestream

    def getTournament():
        tournamentstream = LL_API.getTournament()
        return tournamentstream

    def sort(item):
        """ function to implement keysort for the playersort functions """
        return item[1]

    def getPlayerList(sortkey):
        """ sorts the players according to QPs, Inshots or Outshots. The attribute this functions gets called by should be either of those"""
        players = []
        playerstream = ViewerLL.getPlayers()
        if sortkey == QP:
            sortkey = 5
            """ goes to the item in the list that tracks QPs"""
        if sortkey == inshots:
            sortkey = 6
        if sortkey == outshots:
            sortkey = 7
        for line in playerstream.split(","):
            players[line].append([line[0], line[sortkey]])
            """ gets a list like [[playername, QPs]]"""
        players.sort(key=sort)
        return players

    def getPlayerScore():
        """ Takes the playerstream, finds the player and takes the values from 8-19 and puts them in an array and returns it """
        playerstream = ViewerLL.getPlayers()
        for line in playerstream.split(","):
            if line[0] == playername:
                scores = [line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17], line[18], line[19]]
                """ 501 Einmenn, unnir, tap, 301 Duo, unnir, tap, Cricket, unnir, tap,501 Fjormenn, unnir, tap"""
        return scores

    def getPlayerScoreByDate():
        raise NotImplementedError
    
    def getTournamentScore():
        """ gets all teams in tournament and sorts by games won and rounds won """
        """ NOTE: Implement the sorting so that it sorts by both, as it is it only sorts by games won"""
        tournamentranklist = []
        teamstream = ViewerLL.getTeams()
        for line in teamstream:
            tournamentranklist.append([line[0], line[4], line[5]])
            """ team_name, games won, rounds won """
        tournamentranklist.sort(key=sort)
        return tournamentranklist

    def getTournamentDates():
        """ sækir tournament skrá, fer í línu 2 með dagsetningum og liðum sem spila þann dag og setur í lista """
        tournamentdatelist = []
        tournamentstream = ViewerLL.getTournament()
        for line in tournamentstream:
            if line == 1:
                line.split(",")
                """ google svartagaldur, pls finna betri leið til að taka hvert 3 gildi og setja í list """
                tournamentdatelist = zip(*[iter(line)]*3)
        return tournamentdatelist
    
    def getGameFinished():
        """ Gets finished games by checking whether results have been added. Adds games with results to list"""
        gamestream = ViewerLL.getGames()
        gamesfinished = []
        for line in gamestream.split(","):
            if line[4] != None:
                gamesfinished.append([line[0], line[1], line[3], line[4], line[5], line[6]])
                """ Team 1, Team 2, Date, Winner, ScoreWinner, ScoreLoser"""
        return gamesfinished

    def getUpcomingGames():
        """ Gets upcoming games by checking whether results have been added. Adds games with no results to list"""
        gamestream = ViewerLL.getGames()
        gamesupcoming = []
        for line in gamestream.split(","):
            if line[4] == None:
                gamesupcoming.append([line[0],line[1],line[3]])
                """ Team 1, Team 2, Date"""
        return gamesupcoming
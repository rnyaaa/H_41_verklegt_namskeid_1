from IO_API import IO_API
from logic.PlayersLL import PlayersLL

class LL_API:
    def getPlayers():
        playerstream = IO_API.getAllPlayers()
        return playerstream

    def getTeams():
        teamstream = IO_API.getAllTeams()
        return teamstream

    def getGames():
        gamestream = IO_API.getAllGames()
        return gamestream

    def getTournament():
        tournamentstream = IO_API.getAllTournaments()
        return tournamentstream

    def getResults():
        resultstream = IO_API.getResults()
        return resultstream

    def getPlayerScore(playername = str):
        """ Takes the playerstream, finds the player and takes the values from 8-19 and puts them in an array and returns it """
        playerstream = getPlayers()
        for line in playerstream.split(","):
            if line[0] == playername:
                scores = [line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17], line[18], line[19]]
                """ 501 Einmenn, unnir, tap, 301 Duo, unnir, tap, Cricket, unnir, tap,501 Fjormenn, unnir, tap"""
        return scores

    def getPlayerScoreByDate():
        raise NotImplementedError

    def sort(item):
        """ function to implement keysort for the playersort functions """
        return item[1]

    def getPlayerSortQPInshotsOutshots(sortkey):
        """ sorts the players according to Quality Points """
        players = []
        playerstream = getPlayers()
        if sortkey == QP:
            sortkey = 5
        if sortkey == inshots:
            sortkey = 6
        if sortkey == outshots:
            sortkey = 7
        for line in playerstream.split(","):
            players[line].append(line[0], line[sortkey])
        players.sort(key=sort)
        return players

    def getTournamentScores():
        tournamentscorelist = []
        gamestring = ""
        tournamentstream = getTournament()
        for line in tournamentstream:
            if line == 1:
                line.split(",")
                for item in line
                    """ svartagaldur, pls finnið betri leið til að taka hvert 3 gildi og setja í list """
                    list(zip(*[iter(line)]*3))
                    tournamentscorelist.append(item)
        return tournamentscorelist
                



    def getTournamentDates():
        raise NotImplementedError

    def getGamesFinished():
        """ Gets finished games by checking whether results have been added. Adds games with results to list"""
        gamestream = getGames()
        gamesfinished = []
        for line in gamestream.split(","):
            if line[4] != None:
                gamesfinished.append([line[0], line[1], line[3], line[4], line[5], line[6]])
                """ Team 1, Team 2, Date, Winner, ScoreWinner, ScoreLoser"""
        return gamesfinished

    def getUpcomingGames():
        """ Gets upcoming games by checking whether results have been added. Adds games with no results to list"""
        gamestream = getGames()
        gamesupcoming = []
        for line in gamestream.split(","):
            if line[4] == None:
                gamesupcoming.apepend([line[0],line[1],line[3]])
                """ Team 1, Team 2, Date"""
        return gamesupcoming
        

    def addTeam(newteam):
        IO_API.updateTeams(newteam=str)

    def addGame(gamesupdate):
        IO_API.updateGames(gamesupdate=str)
        
    def addPlayer(name, id_number, home_address, phone_number1, phone_number2, registered_team):
        PlayersLL.addPlayers(name, id_number, home_address, phone_number1, phone_number2, registered_team)

    def changeResults():
        raise NotImplementedError

    def changeDate():
        raise NotImplementedError

    def updatePlayers():
        IO_API.updatePlayers(playerupdate)

    def updateTeams():
        IO_API.updateTeams(teamsupdate=str)

    def updateGames():
        IO_API.updateGames(gamesupdate=str)

    def updateTournament():
        IO_API.updateTournaments(tournamentupdate=str)

    def updateResults():
        IO_API.updateResults(newresults=str, resultsID=str)

from logic.LL_API import LL_API

class ResultsLL():
    def getResults(results=list, resultsID=list):
        resultstream = LL_API.getResults(resultsID)

    def changeResults():
        """ TODO: Fatta hvernig við tökum results úr gagnagrunni, breytum þeim og vistum nýrri útgáfu"""
        """ Þetta þarf líka að geta uppfært player, team og tournament gildi."""
        raise NotImplementedError

    def updateResults(newresults, resultsID):
        players = LL_API.getPlayers()
        games = LL_API.getGames()
        teams = LL_API.getTeams()
        tournament = LL_API.getTournament()

        """ UPDATE QPs """
        for player in players:
            for item in newresults[0]:
                if item == players[player][0]:
                    players[player][5] += newresults[0][item+1]

        """ Update Innskot """
            for item in newresults[1]:
                if item == players[player][0] and players[player][6] < newresults[1][item]:
                    players[player][6] = newresults[1][item]
        
        """ Update Utskot """
            for item in newresults[2]:
                if item == players[player][0] and players[player][7] < newresults[2][item]:
                    players[player][7] = newresults[2][item]

        """ Update Tournament """
            

        """TODO: Fatta hvernig við fáum inn results í LL og hvernig við geymum ný"""
        """ Hvernig á að uppfæra playerr, team og tournament gagnagrunninn út frá þessu?"""
        LL_API.updateResults(newresults, resultsID)
        




        """ uppfæra win ratio, 501 einmenn"""
        resultline = resultstream.readlines()[7:11]
        for player in players:
            for line in resultline:
                for item in resultline:
                    if item == player[0]:
                        player[10] = int(player[10]) + 1

        """ uppfæra win ratio, 301 duo"""
        """ uppfæra win ratio, cricket"""
        """ uppfæra win ratio, 501 fjormenn"""
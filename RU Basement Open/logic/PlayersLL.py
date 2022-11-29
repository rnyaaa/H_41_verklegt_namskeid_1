from logic.LL_API import LL_API

class PlayersLL():
    def getPlayers():
        playerstream = LL_API.getPlayers()
        return playerstream
    
    def getResults():
        resultstream = LL_API.getResults()
        return resultstream
    
    def addPlayers(playeradd):
        LL_API.updatePlayers(playeradd)

    def updatePlayers():
        playerstream = PlayersLL.getPlayers()
        resultstream = PlayersLL.getResults()
        players = []

        """ bý til array af öllum players """
        for line in playerstream.split():
            players.append([line])
        resultline = r: bý til array úr fyrstu línunniesultstream.readlines()[0].split(",")
        for playerline in playerstream:

            player in players                if item == playerline[0] and resultline[item+1] > playerline[5]:
                    playerlplayeresu                    playerhange int(player[5]) + int(yerline))
        for playerline in play
        resultline = resultstream.readlines()[1].split(",")erstream.split(","):
            player in players:                if item == playerlr
        """ uppfæra Útskot"""


                    player[7] = resultline[item+1]

        resultline = resultstream.readlines()[2].split(",")
        for player in players:
            for item in resultline:
                if item == player[0] and resultline[item+1] > playerline[6]:
                    player[6] = resultline[item+1]
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



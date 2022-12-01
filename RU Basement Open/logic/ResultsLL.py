from IO_API import IO_API


class ResultsLL:

    def __init__(self, ioapi_connection: IO_API):
        self.ioapi = ioapi_connection

    def changeResults(resultsID):
        LL_API.getResults(resultsID)

        # Senda svo til UI og fá ný results (newResults) til baka

        ResultsLL.updateResults(newResults, resultsID)

    def updateResults(results, resultsID):
        ResultsLL.updatePlayers(results)
        ResultsLL.updateGames(results)
        ResultsLL.updateTeams(results)
        LL_API.updateResults(results, resultsID)

    def updatePlayers(results):
        players = LL_API.getPlayers()
        for player in players:
            for item in results[0]:
                if item == players[player][0]:
                    players[player][5] += results[0][item+1]

            # Update Innskot
            for item in results[1]:
                if item == players[player][0] and players[player][6] < results[1][item]:
                    players[player][6] = results[1][item]

            # Update Utskot
            for item in results[2]:
                if item == players[player][0] and players[player][7] < results[2][item]:
                    players[player][7] = results[2][item]

            # Update Player Win/Lose Ratio
            # 501 Singles Winners
            for item in results[6]:
                if results[6][item] == players[player][0]:
                    players[player][9] += 1

            # 501 Singles Losers
            for item in results[7]:
                if results[7][item] == players[player][0]:
                    players[player][10] += 1

            # 301 Duo Winners
            for item in results[8]:
                if results[8][item] == players[player][0]:
                    players[player][12] += 1

            # 301 Duo Losers
            for item in results[9]:
                if results[9][item] == players[player][0]:
                    players[player][13] += 1

            # Cricket Winners
            for item in results[10]:
                if results[10][item] == players[player][0]:
                    players[player][15] += 1

            # Cricket Losers
            for item in results[11]:
                if results[11][item] == players[player][0]:
                    players[player][16] += 1

            # 501 Fours Winners
            for item in results[12]:
                if results[10][item] == players[player][0]:
                    players[player][18] += 1

            # 501 Fours Losers
            for item in results[13]:
                if results[11][item] == players[player][0]:
                    players[player][19] += 1

        LL_API.updatePlayers(players)

    def updateGames(results):
        games = LL_API.getGames()
        # Update Games
        # Ok. NÝTT ATTRIBUTE: RESULTS_ID sem tengir við í GAMES og TOURNAMENT modelið
        for game in games:
            if results[14] == games[game][8]:
                # Winner String Update
                games[game][4] = results[5]

                # Winning Score Update
                games[game][5] = results[4][0]

                # Losing Score update
                games[game][6] = results[4][1]

        LL_API.updateGames(games)

    def updateTeams(results):
        teams = LL_API.getTeams()
        # Update Team Score
        # Ok ný regla, winning teamið kemur alltaf fyrst í results á línu 4
        for team in teams:
            if results[3][0] == teams[team][0]:
                teams[team][4] += results[4][0]
                teams[team][5] += results[5][0]

            if results[3][1] == teams[team][0]:
                teams[team][4] += results[4][1]
                teams[team][5] += results[5][0]
        LL_API.updateTeams(teams)

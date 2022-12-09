from logic.LL_API import LL_API
from ui.UI import Menu_functions
from ui.OrganizerUI import OrganizerUI
import os


class ViewerUI:

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayViewerUI(self):
        os.system('cls||clear')
        while True:
            os.system('cls||clear')
            print(78*"_")
            print()
            print(
                "Verið velkomin í Tölfræðivalmyndina!\n\n"

                "➢  Valmynd:\n\n"

                "1.	Listi yfir lið\n"
                "2.	Staða móts\n"
                "3.	Stigatafla yfir leikmenn\n"
                "4.	Stigatafla yfir leikmenn eftir móti\n"
                "5.	Tölfræði fyrir ákveðna leikmenn")

            user_input = Menu_functions.menuFooter(False)
            print("_"*78)

            if user_input == "1":
                self.showTeams()
            elif user_input == "2":
                self.showTournamentInfo()
            elif user_input == "3":
                self.showPlayerHighscore()
            elif user_input == "4":
                self.showPlayerHighscoreTournament()
            elif user_input == "5":
                self.showPlayerStatistics()
            elif user_input == "b":
                break
            elif user_input == "q":
                Menu_functions.menuQuit()
            else:
                print("Ekki gildur valmöguleiki, reyndu aftur")

    def showTeams(self):
        os.system('cls||clear')
        '''Shows list of teams and their players'''
        captain = "Fyrirliði"
        team_player = "Leikmaður"
        teams = self.llapi.getTeams()
        players = self.llapi.getPlayers()
        for team in teams:
            print(f"\nNAFN: {team.name}")
            team_members_count = 0
            for player in players:
                if team.id == player.team_id:
                    team_members_count += 1
                    if team_members_count == 1:
                        print("｜")
                        print(f"｜→     {player.name:<20}{captain:<10}")
                    else:
                        print(f"｜→     {player.name:<20}{team_player:<10}")
            if team_members_count == 0:
                print(f"｜→ Engir leikmenn skráðir.")
        print("\n" + 78*"_")
        user_input = Menu_functions.menuFooter(False)

    def showTournamentInfo(self):
        os.system('cls||clear')
        team_name = "NAFN LIÐS"
        games_won = "UNNIR LEIKIR"
        rounds_won = "UNNIR LEGGIR"

        selected_tournment = OrganizerUI.select_tournament_input(self)
        os.system('cls||clear')
        print()
        #all_games = self.llapi.getGames()

        scores = self.llapi.getTeamScoreSummariesByTournament(
            int(selected_tournment.id))
        scores = list(set(scores))
        scores = sorted(scores, key=lambda x: -x.games_won and -x.rounds_won)
        print(f"       {team_name:<11}｜{games_won:>12}  ｜  {rounds_won:<14}")
        print("-"*78)

        for counter, score in enumerate(scores):
            print(f"{counter+1}. {self.llapi.getTeamNameFromId(score.team_id):>15}｜{score.games_won:>10}    ｜ {score.rounds_won:>10}")

        user_input = Menu_functions.menuFooter(False)

    def showPlayerHighscore(self):
        os.system('cls||clear')
        '''Shows the high score '''
        print("\nListi yfir leikmenn með flestu afreksstig.\n")
        scores = self.llapi.getPlayerScoreSummaries()
        scores = list(set(scores))
        scores = sorted(scores, key=lambda x: -x.QPs)
        print("    NAFN LEIKMANNS        AFREKSSTIG")
        print("-"*78)
        for counter, score in enumerate(scores):
            print(
                f"{counter+1}. {str(self.llapi.getPlayerNameFromId(score.playerid)):<20}  -   {score.QPs:<3}")
        print("-"*78)
        print(
            "1. Stigatafla yfir Innskot\n"
            "2. Stigatafla yfir Útskot"
        )
        user_input = Menu_functions.menuFooter(False)
        if user_input == "1":
            self.showPlayerHighscoreInShot()
        if user_input == "2":
            self.showPlayerHighscoreOutShot()

    def showPlayerHighscoreTournament(self, tournamentid=None):
        os.system('cls||clear')
        '''Shows the high score by Tournament '''
        if tournamentid == None:
            tournament = OrganizerUI.select_tournament_input(self)
            tournamentid = tournament.id
        os.system('cls||clear')
        print(
            f"\nListi yfir leikmenn með flestu afreksstig í {self.llapi.getTournamentNameFromId(tournamentid)}\n")
        scores = sorted(self.llapi.getPlayerScoreSummariesByTournament(
            tournamentid), key=lambda x: -x.QPs)
        print("   NAFN LEIKMANNS          AFREKSSTIG")
        print("_"*78)
        for counter, score in enumerate(scores):
            print(
                f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid):<20}  -  {score.QPs:<4}")
        print("_"*78)
        print()
        print(
            "1. Stigatafla yfir Innskot\n"
            "2. Stigatafla yfir Útskot\n"
        )
        user_input = Menu_functions.menuFooter(False)
        if user_input == "1":
            self.showPlayerHighscoreInShot(tournamentid)
        if user_input == "2":
            self.showPlayerHighscoreOutShot(tournamentid)

    def showPlayerHighscoreInShot(self, tournamentid=None):
        '''Shows the inshot high score '''
        os.system('cls||clear')
        print("\nListi yfir leikmenn með hæsta innskotið.\n")
        print("   NAFN LEIKMANNS          INNSKOT")
        print("-"*78)
        if tournamentid == None:
            scores = self.llapi.getPlayerScoreSummaries()
            scores = list(set(scores))
            scores = sorted(scores, key=lambda x: -x.inshots)
            for counter, score in enumerate(scores):
                print(
                    f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid):<20}  -  {score.inshots:<4}N")
        else:
            scores = sorted(self.llapi.getPlayerScoreSummariesByTournament(
                tournamentid), key=lambda x: -x.inshots)
            for counter, score in enumerate(scores):
                print(
                    f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid):<20}  -  {score.inshots:<4}N")
        print("-"*78)
        print(
            "1. Stigatafla yfir Afreksstig\n"
            "2. Stigatafla yfir Útskot\n"
        )
        user_input = Menu_functions.menuFooter(False)
        if tournamentid == None:
            if user_input == "1":
                self.showPlayerHighscore()
            if user_input == "2":
                self.showPlayerHighscoreOutShot()
        else:
            if user_input == "1":
                self.showPlayerHighscoreTournament(tournamentid)
            if user_input == "2":
                self.showPlayerHighscoreOutShot(tournamentid)

    def showPlayerHighscoreOutShot(self, tournamentid=None):
        '''Shows the outshot high score '''
        os.system('cls||clear')
        print("\nListi yfir leikmenn með hæsta útskotið.\n")
        scores = sorted(self.llapi.getPlayerScoreSummaries(),
                        key=lambda x: -x.outshots)
        print("   NAFN LEIKMANNS          ÚTSKOT")
        print("-"*78)
        if tournamentid == None:
            scores = self.llapi.getPlayerScoreSummaries()
            scores = list(set(scores))
            scores = sorted(scores, key=lambda x: -x.outshots)
            for counter, score in enumerate(scores):
                print(
                    f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid):<20}  -  {score.outshots:<4}U")
        else:
            scores = sorted(self.llapi.getPlayerScoreSummariesByTournament(
                tournamentid), key=lambda x: -x.outshots)
            for counter, score in enumerate(scores):
                print(
                    f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid):<20}  -  {score.outshots:<4}U")
        print("-"*78)
        print(
            "1. Stigatafla yfir Afreksstig\n"
            "2. Stigatafla yfir Innskot\n"
        )
        user_input = Menu_functions.menuFooter(False)
        if tournamentid == None:
            if user_input == "1":
                self.showPlayerHighscore()
            if user_input == "2":
                self.showPlayerHighscoreInShot()
        else:
            if user_input == "1":
                self.showPlayerHighscoreTournament(tournamentid)
            if user_input == "2":
                self.showPlayerHighscoreInShot(tournamentid)

    def showPlayerStatistics(self):
        """Shows statistics for a selected player"""
        os.system('cls||clear')
        players = self.llapi.getPlayers()
        command = None
        print()
        print("------------Allir leikmenn--------------")
        print()
        while command == None:
            for i in range(len(players)):
                print(f"{i+1:>4}.  {players[i].name}")
            print("-"*78)
            command = int(input(
                f"\nVeldu leikmann af listanum hér fyrir ofan (sláðu t.d. inn 1 fyrir {players[0].name}): "))
        os.system('cls||clear')
        print(f"\nTölfræði fyrir {players[command-1].name}\n")
        statistics = self.llapi.getSinglePlayerScore(
            players[command-1].playerid)
        try:
            print(f"QPs overall: {statistics.QPs}")
            print(f"Largest inshot: {statistics.inshots}")
            print(f"Largest outshot: {statistics.outshots}")
            print(
                f"501 singles win/loss ratio: {statistics.result501singles[0]} / {statistics.result501singles[1]}")
            print(
                f"301 win/loss ratio: {statistics.result301[0]} / {statistics.result301[1]}")
            print(
                f"cricket win/loss ratio: {statistics.resultcricket[0]} / {statistics.resultcricket[1]}")
            print(
                f"501 fours win/loss ratio: {statistics.result501fours[0]} / {statistics.result501fours[1]}")
            print(
                f"\n0. Sýna tölfræði {players[command-1].name} eftir dagsetningu")
        except:
            print(
                "!!! Leikmaður hefur ekki spilað nógu mikið af leikjum til að birta tölfræði !!!")
        user_input = Menu_functions.menuFooter(False)
        if user_input == "0":
            self.getPlayerScoreByDate(players[command-1])

    def getPlayerScoreByDate(self, player):
        """Prints a list of all players and their scores by dates."""
        os.system('cls||clear')
        games = self.llapi.getGamesFinished()
        command = None
        while command == None:
            for i in range(len(games)):
                print(i+1, ". ", games[i].date,
                      games[i].home_team, "vs.", games[i].away_team)
            command = int(input(f"\nVeldu dagsetningu leiks: "))

        os.system('cls||clear')
        print(f"\nTölfræði {player.name} síðan {games[command-1].date}:\n")
        statistics = self.llapi.getPlayerScoreByDate(
            player.playerid, games[command-1].date)
        print(f"QPs overall: {statistics.QPs}")
        print(f"Largest inshot: {statistics.inshots}")
        print(f"Largest outshot: {statistics.outshots}")
        print(
            f"501 singles win/loss ratio: {statistics.result501singles[0]} / {statistics.result501singles[1]}")
        print(
            f"301 win/loss ratio: {statistics.result301[0]} / {statistics.result301[1]}")
        print(
            f"cricket win/loss ratio: {statistics.resultcricket[0]} / {statistics.resultcricket[1]}")
        print(
            f"501 fours win/loss ratio: {statistics.result501fours[0]} / {statistics.result501fours[1]}")
        user_input = Menu_functions.menuFooter(False)

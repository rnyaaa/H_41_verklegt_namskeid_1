from logic.LL_API import LL_API
from ui.UI import Menu_functions
from ui.OrganizerUI import OrganizerUI

class ViewerUI:

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayViewerUI(self):
        while True:
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
        team_name = "NAFN LIÐS"
        games_won = "UNNIR LEIKIR"
        rounds_won = "UNNIR LEGGIR"
        
        selected_tournment = OrganizerUI.select_tournament_input(self)
        print()
        #all_games = self.llapi.getGames()
        
        scores = sorted(self.llapi.getTeamScoreSummaries(int(selected_tournment.id)), key=lambda x: -x.games_won)
        print(f"    {team_name:<11}｜{games_won:>15}  ｜  {rounds_won:<14}")
        print("-"*78)
        
        for counter, score in enumerate(scores):
            #if selected_tournment.id == score.id:
            print(f"{counter+1}. {self.llapi.getTeamNameFromId(score.team_id):>12}｜{score.games_won:>10}       ｜      {score.rounds_won:<12}")

        '''home, score, away = "Heimalið 🏠", "Úrslit 🎯", "Útilið 🚌"
        print(f"{home:>19}" + "｜" + f"{score:^11}" +
              "｜" + f"{away:<20}")
        print("     " + 50*"-")'''
        
        '''for game in all_games:
            if game.tournament_id == selected_tournment.id:
                print(
                    f"{game.home_team:>20}" + "｜" + f"{game.results:^12}" + "｜" + f"{game.away_team:<20}")'''

        user_input = Menu_functions.menuFooter(False)

    def showPlayerHighscore(self):
        '''Shows the high score '''
        print("\nListi yfir leikmenn með flestu afreksstig.\n")
        scores = sorted(self.llapi.getPlayerScoreSummaries(), key=lambda x: -x.QPs)
        print("    NAFN LEIKMANNS           AFREKSSTIG\n")
        for counter, score in enumerate(scores):
            print(f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid):<20}  -   {score.QPs:<3}")
        print()
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
        '''Shows the high score by Tournament '''
        if tournamentid == None:
            tournament = OrganizerUI.select_tournament_input(self)
        print(tournament.id)
        print(f"\nListi yfir leikmenn með flestu afreksstig í {tournament.name}\n")
        scores = sorted(self.llapi.getPlayerScoreSummariesByTournament(tournament.id), key=lambda x: -x.QPs)
        print("   NAFN LEIKMANNS           AFREKSSTIG\n")
        for counter, score in enumerate(scores):
            print(f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid)}  -   {score.QPs}")
        print()
        print(
            "1. Stigatafla yfir Innskot\n"
            "2. Stigatafla yfir Útskot\n"
        )
        user_input = Menu_functions.menuFooter(False)
        if user_input == "1":
            self.showPlayerHighscoreInShot(tournament.id)
        if user_input == "2":
            self.showPlayerHighscoreOutShot(tournament.id)
    def showPlayerHighscoreViewer(self):
        print("Listi yfir leikmenn með flestu afreksstig.")

        scores = sorted(self.llapi.getPlayerScores(), key=lambda x: x.QPs)
        for counter, score in enumerate(scores):
            print(
                f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid)}  -   {score.QPs}")

        print("_"*78)

    def showPlayerHighscoreInShot(self, tournamentid=None):
        '''Shows the inshot high score '''
        print("\nListi yfir leikmenn með hæsta innskotið.\n")
        print("   NAFN LEIKMANNS          INNSKOT\n")
        if tournamentid == None:
            scores = sorted(self.llapi.getPlayerScoreSummaries(), key=lambda x: -x.inshots)
            for counter, score in enumerate(scores):
                print(f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid):<20}  -  U{score.inshots:<4}")
        else: 
            scores = sorted(self.llapi.getPlayerScoreSummariesByTournament(tournamentid), key=lambda x: -x.inshots)
            for counter, score in enumerate(scores):
                print(f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid):<20}  -  U{score.inshots:<4}")
        print()
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
        print("\nListi yfir leikmenn með hæsta útskotið.\n")
        scores = sorted(self.llapi.getPlayerScoreSummaries(), key=lambda x: -x.outshots)
        print("   NAFN LEIKMANNS           ÚTSKOT\n")
        if tournamentid == None:
            scores = sorted(self.llapi.getPlayerScoreSummaries(), key=lambda x: -x.outshots)
            for counter, score in enumerate(scores):
                print(f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid):<20}  -  U{score.outshots:<4}")
        else:
            scores = sorted(self.llapi.getPlayerScoreSummariesByTournament(tournamentid), key=lambda x: -x.outshots)
            for counter, score in enumerate(scores):
                print(f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid):<20}  -  U{score.outshots:<4}")
        print()
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
        players = self.llapi.getPlayers()
        command = None
        while command == None:
            for i in range(len(players)):
                print(i+1, ". ", players[i].name)
            command = int(input(f"\nVeldu leikmann af listanum hér fyrir ofan (sláðu t.d. inn 1 fyrir {players[0].name}): "))
        print(f"\nTölfræði fyrir {players[command-1].name}\n")
        statistics = self.llapi.getSinglePlayerScore(players[command].playerid)
        print(f"QPs overall: {statistics.QPs}")
        print(f"Largest inshot: {statistics.inshots}")
        print(f"Largest outshot: {statistics.outshots}")
        print(f"501 singles win/loss ratio: {statistics.result501singles[0]} / {statistics.result501singles[1]}")
        print(f"301 win/loss ratio: {statistics.result301[0]} / {statistics.result301[1]}")
        print(f"cricket win/loss ratio: {statistics.resultcricket[0]} / {statistics.resultcricket[1]}")
        print(f"501 fours win/loss ratio: {statistics.result501fours[0]} / {statistics.result501fours[1]}")

        user_input = Menu_functions.menuFooter(False)
        print("_"*78)


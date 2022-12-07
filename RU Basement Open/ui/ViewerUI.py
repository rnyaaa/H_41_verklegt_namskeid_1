from logic.LL_API import LL_API
from ui.UI import Menu_functions
from ui.OrganizerUI import OrganizerUI
from models.player import Player
from models.team import Team
from models.tournament import Tournament
from operator import itemgetter
from models.playersummary import PlayerSummary

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
                "3.	Listi yfir þá sem hafa skorað flest afreksstig (QPs)\n"
                "4.	Listi yfir þá sem eiga besta/hæsta innskotið á mótinu/deildinni\n"
                "5.	Listi yfir þá sem eiga besta/hæsta útskotið á mótinu/deildinni\n"
                "6.	Tölfræði fyrir ákveðna leikmenn")

            user_input = Menu_functions.menuFooter(False)
            print("_"*78)

            if user_input == "1":
                self.showTeams()
            elif user_input == "2":
                self.showTournamentInfo()
            elif user_input == "3":
                self.showPlayerHighscoreQP()
            elif user_input == "4":
                self.showPlayerHighscoreInShot()
            elif user_input == "5":
                self.showPlayerHighscoreOutShot()
            elif user_input == "6":
                self.showPlayerStatistics()
            elif user_input == "b":
                break
            elif user_input == "q":
                Menu_functions.menuQuit()
            else:
                print("Ekki gildur valmöguleiki, reyndu aftur")

    def showTeams(self):
        '''Shows list of teams and their players'''
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
                        print(f"｜→     {player.name:<15} {player.home_phone:<7} {player.playerid:^10} {player.address:<20}Fyrirliði")
                    else:
                        print(f"｜→     {player.name:<15} {player.home_phone:<7} {player.playerid:^10} {player.address:<20}Leikmaður")
            if team_members_count == 0:
                print(f"｜→ Engir leikmenn skráðir.")
        print("\n" + 78*"_")
        user_input = Menu_functions.menuFooter(False)

    def showTournamentInfo(self):
        # Á þetta kanski að vera listi yfir sigra hjá hverju liði en ekki á móti hvor öðru?
        selected_tournment = OrganizerUI.select_tournament_input(self)
        print()
        all_games = self.llapi.getGames()
        home, score, away = "Heimalið 🏠", "Úrslit 🎯", "Útilið 🚌"
        print(f"{home:>19}" + "｜" + f"{score:^11}" +
              "｜" + f"{away:<20}")
        print("     " + 50*"-")
        for game in all_games:
            if game.tournament_id == selected_tournment.id:
                print(
                    f"{game.home_team:>20}" + "｜" + f"{game.results:^12}" + "｜" + f"{game.away_team:<20}")
        user_input = Menu_functions.menuFooter(False)

    def showPlayerHighscoreQP(self):
        '''Shows the high score '''
        print("\nListi yfir leikmenn með flestu afreksstig.\n")
        scores = sorted(self.llapi.getPlayerScores(), key=lambda x: -x.QPs)
        print("    Nafn leikmanns  Afreksstig")
        for counter, score in enumerate(scores):
            print(f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid)}  -   {score.QPs}")
        user_input = Menu_functions.menuFooter(False)
        print("_"*78)

    def showPlayerHighscoreInShot(self):
        '''Shows the high score '''
        select_tournament = OrganizerUI.select_tournament_input(self)
        print("\nListi yfir leikmenn með hæsta innskotið.\n")
        # hér:
        scores = sorted(self.llapi.getPlayerScores(), key=lambda x: -x.inshots)
        if select_tournament.id == scores.tournamentid:
            for counter, score in enumerate(scores):
                print(f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid)}  -  I{score.inshots}")
        user_input = Menu_functions.menuFooter(False)
        print("_"*78)
    
    
    def showPlayerHighscoreOutShot(self):
        '''Shows the high score '''
        print("\nListi yfir leikmenn með flestu afreksstig.\n")
        # hér:
        scores = sorted(self.llapi.getPlayerScores(), key=lambda x: -x.outshots)
        for counter, score in enumerate(scores):
            print(f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid)}  -  U{score.outshots}")

        user_input = Menu_functions.menuFooter(False)
        print("_"*78)
    
    
    def showPlayerStatistics(self):
        """Shows statistics for a selected player"""
        players = self.llapi.getPlayers()
        command = None
        while command == None:
            for i in range(len(players)):
                print(i+1, ". ", players[i].name)
            command = int(input(f"\nVeldu leikmann af listanum hér fyrir ofan (sláðu t.d. inn 1 fyrir {players[0].name}): "))
        print(f"\nTölfræði fyrir {players[command].name}\n")
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


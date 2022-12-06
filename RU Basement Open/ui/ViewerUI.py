from logic.LL_API import LL_API
from ui.UI import Menu_functions
from ui.OrganizerUI import OrganizerUI
from models.player import Player
from models.team import Team
from models.tournament import Tournament
from operator import itemgetter


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
                self.showPlayerHighscoreViewer()
            elif user_input == "4":
                self.showPlayerHighscoreViewer()
            elif user_input == "5":
                self.showPlayerHighscoreViewer()
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
            print(f"\n👥 {team.name}")
            team_members_count = 0
            for player in players:
                if team.id == player.team_id:
                    team_members_count += 1
                    if team_members_count == 1:
                        print("｜")
                        print(f"｜→     {player.name} // 🐐 fyrirliði")
                    else:
                        print(f"｜→     {player.name}")
            if team_members_count == 0:
                print(f"｜→ Engir leikmenn skráðir.")

        print("\n" + 78*"_")
        user_input = Menu_functions.menuFooter(False)

    def showTournamentInfo(self):
<<<<<<< HEAD
        pass

=======
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
>>>>>>> 1af97ae9054bd17494cce43d814eb7761d90d0fc

        user_input = Menu_functions.menuFooter(False)

    def showPlayerHighscoreViewer(self):
        player_dict = {}
        print("Listi yfir leikmenn með flestu afreksstig.")

        high_score = self.llapi.getPlayerScores()
        # print(high_score)
        """
        counter = 1

        for player in high_score:
            for score in player:
                player_dict[score.QPs] = score.playerid

        player_dict = sorted(player_dict)
        for key, val in player_dict:
            print(f"{counter}. {val} - {key}")
            counter +=1
        
        """

        """sorted_score = sorted(high_score, key=itemgetter(2))
        for player in sorted_score:
            for points in player:
                print(f"{counter}. {points.playerid}  -   {points.QPs}")
                counter += 1"""

        # hér:
        scores = sorted(self.llapi.getPlayerScores(), key=lambda x: x.QPs)
        for counter, score in enumerate(scores):
            print(f"{counter+1}. {self.llapi.getPlayerNameFromId(score.playerid)}  -   {score.QPs}")

        print("_"*78)

    def showPlayerStatistics(self):
        """Shows statistics for a selected player"""
        players = self.llapi.getPlayers()
        while True:
            for i in range(len(players)):
                print(i+1, ". ", players[i].name)
            command = int(input(
                f"\nVeldu leikmann af listanum hér fyrir ofan (sláðu t.d. inn 1 fyrir {players[0].name}): "))
            print(f"\nTölfræði fyrir {players[i].name}\n")

from IO.IO_API import IO_API
from models.team import Team


class TeamsLL:

    def __init__(self, ioapi_connection: IO_API):
        self.ioapi = ioapi_connection

    def get_all_teams(self):
        teams = self.ioapi.getAll("teams")
        team_models = []
        for lis in teams:
            team_models.append(
                # id, team_name, address, association_name, phone_nr, total_games_won, total_rounds_won, player1, player2, player3, player4
                Team(lis[0], lis[1], lis[2], lis[3], lis[4], lis[5], lis[6], lis[7], lis[8], lis[9], lis[10], lis[11]))
        return team_models

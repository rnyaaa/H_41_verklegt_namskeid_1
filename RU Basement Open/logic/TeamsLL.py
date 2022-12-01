from IO_API import IO_API


class Teams:
    
    def __init__(self, ioapi_connection: IO_API):
        self.ioapi = ioapi_connection

    def get_all_players(self):
        teams = self.ioapi.getAll("teams")
        team_models = []
        for lis in teams:
            team_models.append(
                Player(lis[0], lis[1], lis[2], lis[3], lis[4]))
        return team_models
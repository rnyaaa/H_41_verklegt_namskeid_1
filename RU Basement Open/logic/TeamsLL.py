from IO.IO_API import IO_API
from models.team import Team


class TeamsLL:

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def get_all_teams(self):
        return self.ioapi.return_model(Team)
        

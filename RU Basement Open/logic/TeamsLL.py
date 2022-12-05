from IO.IO_API import IO_API
from models.team import Team

class TeamsLL:

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def getAllTeams(self) -> list[Team]:
        """ returns a list of all Team instances """
        return self.ioapi.return_model(Team)

    def addTeam(self, team: Team):
        """ adds a team """
        return self.ioapi.create_model(Team)
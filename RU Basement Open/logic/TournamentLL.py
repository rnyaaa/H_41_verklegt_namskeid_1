from IO.IO_API import IO_API
from models.tournament import Tournament
from models.team import Team

class TournamentLL():
    
    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def addTournament(self):
        tournaments = self.ioapi.getTournament()

    def getTournamentScore(self):
        teams = self.ioapi.return_model(Team)
        raise NotImplementedError

    def getTournamentDates(self):
        tournaments = self.ioapi.return_model(Tournament)
        raise NotImplementedError

from IO.IO_API import IO_API
from models.tournament import Tournament
from models.team import Team
from models.game import Game


class TournamentLL():

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def getAllTournaments(self) -> list[Tournament]:
        """Returns a list of all Tournament instances."""
        return self.ioapi.return_model(Tournament)

    def addTournament(self, tournament: Tournament):
        """Add a tournament."""
        return self.ioapi.create_model(tournament)

    def getTournamentNameFromId(self, tournamentid):
        """Gets a tournament name for a given tourment id."""
        tournaments = self.getAllTournaments()
        for tournament in tournaments:
            if tournament.id == tournamentid:
                return tournament.name

    def changeTournamentInfo(self, updated_info: Tournament):
        """Update tournament info."""
        self.ioapi.update(updated_info)
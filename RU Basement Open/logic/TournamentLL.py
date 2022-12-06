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

    def getTournamentScore(self):
       """Returns a list of tuples containing the team name, games won and rounds won."""
        all_games = self.ioapi.return_model(Game)
        wins = 0 
        rounds_won = 0
        for game in all_games:
            for i in range(len())
            rounds_won += game.results[0]
            if int(game.results[0]) > int(game.results[2]):
                wins+=1
            
            return [game.home_team[wins, ]]
            

    def changeTournamentInfo(self, updated_info: Tournament):
        self.ioapi.overwrite_model(updated_info)




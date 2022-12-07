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
        tournaments = self.getAllTournaments()
        for tournament in tournaments:
            if tournament.id == tournamentid:
                return tournament.name

    def getTournamentScore(self):
        """
        Returns a list of tuples containing the team name, games won and rounds won.
        """

        all_games = self.ioapi.return_model(Game)
        teams_rounds_wins = {}
        teams_matches_wins = {}
        
        for game in all_games:
            if game.home_team not in teams_rounds_wins:
                teams_rounds_wins[game.home_team] = 0
            teams_rounds_wins[game.home_team] += int(self.result.split("-")[0])
            #########
            if game.home_team not in teams_matches_wins:
                teams_matches_wins[game.home_team] = 0
            if int(self.result.split("-")[0]) == 2:
                teams_matches_wins[game.home_team] += 1

            ##############################

            if game.away_team not in teams_rounds_wins:
                teams_rounds_wins[game.away_teams] = 0
            teams_rounds_wins[game.away_teams] += int(self.result.split("-")[1])
            #########
            if game.away_teams not in teams_matches_wins:
                teams_matches_wins[game.away_teams] = 0
            if int(self.result.split("-")[1]) == 2:
                teams_matches_wins[game.away_teams] += 1
        
        return teams_matches_wins, teams_rounds_wins

    def changeTournamentInfo(self, updated_info: Tournament):
        self.ioapi.update(updated_info)




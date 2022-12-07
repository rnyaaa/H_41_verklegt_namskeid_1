class Game:
    def __init__(self, game_id=None, tournament_id=None, home_team=None, away_team=None, date=None, results_hometeam=None, results_awayteam=None):
        self.gameid = game_id
        self.tournament_id = tournament_id
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.results_hometeam = results_hometeam
        self.results_awayteam = results_awayteam

    def listify(self):
        return [self.gameid, self.tournament_id, self.home_team, self.away_team, self.date, self.results_hometeam, self.results_awayteam]

    def model(self):
        return "games"

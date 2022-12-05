class Game:
    def __init__(self,tournament_id = '',game_id = '',home_team='', away_team='', date = '', results = ''):
        self.gameid = game_id
        self.tournament_id = tournament_id
        self.date = date
        self.results = results
        self.home_team = home_team
        self.away_team = away_team

    def listify(self):
        return [self.gameid, self.tournament_id, self.home_team, self.away_team, self.date, self.results]

    def model(self):
        return "games"
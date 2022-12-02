class Game:
    def __INIT__(self, game_id, tournament_id, date, results):
        self.gameid = game_id
        self.tournament_id = tournament_id
        self.date = date
        self.results = results

    def listify(self):
        return [self.gameid, self.tournament_id, self.date, self.results]

    def model(self):
        return "games"
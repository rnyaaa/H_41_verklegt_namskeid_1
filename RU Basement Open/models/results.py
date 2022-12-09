class Results:
    def __init__(self, game_id, results_id, team_ids, winningscore, losingscore):
        self.game_id = game_id
        self.results_id = results_id
        self.teams = team_ids
        self.winningscore = winningscore
        self.losingscore = losingscore

    def listify(self):
        """Returns the model on a list form."""
        return [self.game_id, self.results_id, *self.teams, *self.winningscore, *self.losingscore]

    def model(self):
        return "Results"

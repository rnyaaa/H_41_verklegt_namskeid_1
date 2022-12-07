class TeamScore:
    
    def __init__(
        self, 
        tournament_id=None,
        team_id=None,
        game_id=None,
        games_won=None, 
        rounds_won=None):
        self.tournament_id = tournament_id
        self.team_id = team_id
        self.game_id = game_id
        self.games_won = games_won
        self.rounds_won = rounds_won


    def listify(self):
        return [self.tournament_id, self.team_id, self.game_id, self.games_won, self.rounds_won]

    def model(self):
        return "teamscore"

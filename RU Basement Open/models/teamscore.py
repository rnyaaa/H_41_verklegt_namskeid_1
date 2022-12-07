class TeamScore:
    
    def __init__(
        self, 
        team_id=None,
        tournament_id=None,
        game_id=None,
        games_won=0, 
        rounds_won=0):
        self.team_id = team_id
        self.tournament_id = tournament_id
        self.game_id = game_id
        self.games_won = games_won
        self.rounds_won = rounds_won


    def listify(self):
        return [self.team_id, self.tournament_id, self.game_id, self.games_won, self.rounds_won]

    def model(self):
        return "teamscore"

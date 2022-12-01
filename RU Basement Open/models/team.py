class Team:
    def __INIT__(self, id='', name='', address='', club_name='', phone='', games_won='', rounds_won='', players=[]):
        self.id = id
        self.name = name
        self.address = address
        self.club_name = club_name
        self.phone = phone
        self.games_won = games_won
        self.rounds_won = rounds_won
        self.players = players

    def listify(self):
        return [self.id, self.name, self.address, self.club_name, self.phone, self.games_won, self.rounds_won, self.players]

    def model(self):
        return "teams"
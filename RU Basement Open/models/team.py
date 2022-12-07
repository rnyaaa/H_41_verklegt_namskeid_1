class Team:
    def __init__(self, id='', name='', address='', club_name='', phone='', games_won='', rounds_won='', player1='', player2='', player3='', player4=''):
        self.id = id
        self.name = name
        self.address = address
        self.club_name = club_name
        self.phone = phone
        self.games_won = games_won
        self.rounds_won = rounds_won


    def listify(self):
        return [self.id, self.name, self.address, self.club_name, self.phone, self.games_won, self.rounds_won]

    def model(self):
        return "teams"

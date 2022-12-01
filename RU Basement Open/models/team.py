class Team:
    def __INIT__(self, id='', name='', address='', club_name='', phone='', games_won='', rounds_won='', player1='', player2='', player3='', player4=''):
        self.id = id
        self.name = name
        self.address = address
        self.club_name = club_name
        self.phone = phone
        self.games_won = games_won
        self.rounds_won = rounds_won
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4

    def listify(self):
        return [self.id, self.name, self.address, self.club_name, self.phone, self.games_won, self.rounds_won, [self.player1, self.player2, self.player3, self.player4]]

    def model(self):
        return "teams"

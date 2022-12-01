class Tournament:
    def __INIT__(self="", name="", organizer_name="", organizer_phone="", games=[], teams=[]):
        self.name = name
        self.organizer_name = organizer_name
        self.organizer_phone = organizer_phone
        self.games = games
        self.teams = teams

    def listify(self):
        return [[self.name, self.organizer_name, self.organizer_phone], self.games, self.teams]

    def model(self):
        return "tournaments"
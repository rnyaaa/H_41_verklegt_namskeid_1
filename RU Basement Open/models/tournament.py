class Tournament:
    def __init__(self, name="", organizer_name="", organizer_phone="",tournament_type="", games=[], teams=[]):
        self.name = name
        self.organizer_name = organizer_name
        self.organizer_phone = organizer_phone
        self.tournament_type =tournament_type
        self.games = games
        self.teams = teams

    def listify(self):
        return [[self.name, self.organizer_name, self.organizer_phone, self.tournament_type], self.games, self.teams]

    def model(self):
        return "tournaments"
class Tournament:
    def __init__(self, name="", organizer_name="", organizer_phone="", date_list="", games="", teams=""):
        self.name = name
        self.organizer_name = organizer_name
        self.organizer_phone = organizer_phone
        self.date = date_list
        self.games = games
        self.teams = teams

    def listify(self):
        return [self.name, self.organizer_name, self.organizer_phone, self.date, self.games, self.teams]

    def model(self):
        return "tournaments"
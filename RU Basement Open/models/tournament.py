class Tournament:
    def __init__(self, id="", name="", organizer_name="", organizer_phone="", date_list=[], games_list=[], teams_list=[]):
        self.id = id
        self.name = name
        self.organizer_name = organizer_name
        self.organizer_phone = organizer_phone
        self.date_list = date_list
        self.games_list = games_list
        self.teams_list = teams_list

    def listify(self):
        return [self.id, self.name, self.organizer_name, self.organizer_phone, self.date_list, self.games_list, self.teams_list]

    def model(self):
        return "tournaments"
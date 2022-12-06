class Tournament:

    def __init__(self, id="", name="", organizer_name="", organizer_phone="", start_date="", end_date=""):
        self.id = id
        self.name = name
        self.organizer_name = organizer_name
        self.organizer_phone = organizer_phone
        self.start_date = start_date
        self.end_date = end_date

    def listify(self):
        return [self.id, self.name, self.organizer_name, self.organizer_phone, self.start_date, self.end_date]

    def model(self):
        return "tournaments"

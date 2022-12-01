class Player:
    def __init__(self, id="", name="", birth_year="", phone_nr="", email=""):
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.phone_nr = phone_nr
        self.email = email

    def listify(self):
        return [self.id, self.name, self.birth_year, self.phone_nr, self.email]

    def model(self):
        return "players"

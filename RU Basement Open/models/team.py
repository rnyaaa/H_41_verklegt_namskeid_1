class Team:
    def __init__(self, id='', name='', address='', club_name='', phone='' ):
        self.id = id
        self.name = name
        self.address = address
        self.club_name = club_name
        self.phone = phone


    def listify(self):
        return [self.id, self.name, self.address, self.club_name, self.phone]

    def model(self):
        return "teams"

class Player:
    def __init__(self, playerid, name, mobile, home_phone, address):
        self.playerid = playerid
        self.name = name
        self.mobile = mobile
        self.home_phone = home_phone
        self.address = address

    def listify(self):
        return [self.playerid, self.name, self.mobile, self.home_phone, self.address]

    def model(self):
        return "players"